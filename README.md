# Mechanism reduction using directed relation graph (DRG)
- Uses PSR (perfectly stirred reactor) to span the chemical state including the unstable branch of the S-curve
- Uses Cantera for thermochemical properties
- Uses Sundials Kinsol for solving the system of equations
- Input a detailed chemical mechanism and produce a skeletal mechanism based on tolerance for species dependencies.

![S-curve](docs/images/S_curve.png)


## Build, run
- ```mkdir build```
- ```cd build```
- ```cmake ..```
- ```make```
- ```make install```
- ```cd ../run```
- ```./bones.x```

The user parameters are read from `../input/input.yaml`, or specify a different path/file.yaml as an argument.
