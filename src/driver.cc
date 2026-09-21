#include "psr.h"
#include "drg.h"
#include "streams.h"
#include "cantera/base/AnyMap.h"

#include <string>
#include <iostream>

using namespace std;
using namespace Cantera;

////////////////////////////////////////////////////////////////////////////////

int main(int argc, char** argv) {

    //--------------- input file

    string inputName = argc > 1 ? argv[1] : "../input/input.yaml";
    AnyMap input = AnyMap::fromYamlFile(inputName);

    const AnyMap& inp_mech    = input["mechanism"].as<AnyMap>();
    const AnyMap& inp_drg     = input["drg"].as<AnyMap>();
    const AnyMap& inp_streams = input["streams"].as<AnyMap>();
    const AnyMap& inp_mixfrac = input["mixture_fraction"].as<AnyMap>();
    const AnyMap& inp_psr     = input["psr"].as<AnyMap>();

    //--------------- user inputs

    string mechName            = inp_mech.getString("detailed", "gri30.yaml");
    string skMechName          = inp_mech.getString("skeletal", "skel.yaml");
    double eps                 = inp_drg.getDouble("tolerance", 0.3);
    vector<string> spPrincipal = inp_drg["principal_species"].as<vector<string>>();
    vector<string> spExtra     = inp_drg["extra_species"].as<vector<string>>();

    double P  = inp_streams.getDouble("pressure", 101325);
    double T0 = inp_streams.getDouble("temperature", 300);
    string x0 = inp_streams.getString("oxidizer_composition", "O2:2, N2:7.52");
    string x1 = inp_streams.getString("fuel_composition", "CH4:1");

    int nmixf        = inp_mixfrac.getInt("count", 11);
    double mixfstart = inp_mixfrac.getDouble("start", 0.03);
    double mixfend   = inp_mixfrac.getDouble("end", 0.07);

    int    nT        = inp_psr.getInt("temperature_count", 201);
    double Tmin      = inp_psr.getDouble("minimum_temperature", 1000);
    double TmaxDelta = inp_psr.getDouble("maximum_temperature_delta", -5.1);
    double taug      = inp_psr.getDouble("initial_tau", 0.01);

    //--------------- initialize cantera

    double T1 = T0;                  // two streams for composition, but one psr inlet

    auto sol = newSolution(mechName, "", "none");
    auto gas = sol->thermo();
    auto kin = sol->kinetics();

    size_t nsp  = gas->nSpecies();

    DRG drg(gas, kin, spPrincipal, spExtra, eps);

    //--------------- initialize streams

    gas->setState_TPX(T0, P, x0);
    double h0 = gas->enthalpy_mass();
    vector<double> y0(nsp);
    gas->getMassFractions(&y0[0]);

    gas->setState_TPX(T1, P, x1);
    double h1 = gas->enthalpy_mass();
    vector<double> y1(nsp);
    gas->getMassFractions(&y1[0]);

    streams strm(gas, P, T0, T1, x0, x1);

    //--------------- storage arrays

    vector<double> yin(nsp);
    double         hin;

    vector<double> yad(nsp);
    double         had;
    double         Tad;

    //--------------- PSR object, scaling arrays

    PSR psr(gas, kin);

    vector<double> y_tau_scale(nsp+1, 1.0);
    vector<double> f_scale(nsp+1, 1.0);

    //--------------- solve the psr for each composition

    vector<double> mixfvec(nmixf);
    for(int i=0; i<nmixf; i++)
        mixfvec[i] = mixfstart + (double)(i)/(nmixf-1) * (mixfend - mixfstart);

    cout << endl << "Solving full PSR S-curve for the following mixture fractions: ";

    double Tdmb;

    for(int imixf=0; imixf<nmixf; imixf++) {               // LOOP over each composition

        strm.getMixingState(   mixfvec[imixf], yin, hin, Tdmb);
        strm.getEquilibrium_HP(mixfvec[imixf], yad, had, Tad);

        psr.setInlet(yin, hin, P);

        cout << endl << mixfvec[imixf];

        //--------------- solve psr for each T for given composition

        double Tmax = Tad + TmaxDelta;      // this can be 0.1 or 0.01 for stoich methane/air, but higher like 5 or more for lean to 0.03 mixf
        vector<double> Tvec(nT);      // temperature values
        for(int i=0; i<nT; i++)
            Tvec[i] = Tmax - (double)(i)/(nT-1) * (Tmax - Tmin);

        vector<double> y_tau = yad;   // unknown vector: species mass fractions and tau
        y_tau.push_back(taug);

        for(int i=0; i<nT; i++) {                          // LOOP over each temperature
            psr.setT(Tvec[i]);
            psr.solvePSR(y_tau, y_tau_scale, f_scale);     // solve psr at this point

            gas->setState_TPY(Tvec[i], P, &y_tau[0]);
            drg.DRGspeciesSet();
        }
    }

    //--------------- output the skeletal species

    cout << endl;
    cout << endl << "Cantera mechanism name: " << sol->name();
    cout << endl << "DRG tolerance: " << eps;

    //--------------- create skeletal mechanism

    drg.writeSkeletalMechanism(mechName, skMechName);

    return 0;
}
