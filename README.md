# Mechanism reduction using directed relation graph (DRG)
* Uses PSR (perfectly stirred reactor) to span the chemical state
* Uses Cantera for thermochemical properties
    * Note, Cantera was built with Sundials installed separately
* Uses Sundials Kinsol for solving the system of equations

## Build, run
* ```mkdir build```
* ```cd build```
* ```cmake ..```
* ```make```
* ```make install```
* ```cd ../run```
* ```./drg.x input/input.yaml```

The user parameters are read from `input/input.yaml`. The executable defaults
to that filename, so `./drg.x` is also sufficient from the project root or the
installed `run` directory.
