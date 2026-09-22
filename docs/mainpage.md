
\mainpage

<!-- #################################################################### -->

# Overview

[Bones](https://github.com/BYUignite/bones.git) is a C++ code for computing skeletal mechanisms using the Directed Relation Graph (DRG) method. The code reduces a detailed mechanism to a skeletal mechanism by removing species and reactions that are deemed unimportant for the target species. The code is designed to be flexible and extensible, allowing users to easily modify the reduction criteria and add new features. The reduction is done using the full S-curve of a perfectly stirred reactor (PSR) simulation, solved with several stoichiometric ratios. The skeletal mechanism in Cantera format is output to a file.

# Dependencies and installation

The code is intended to be built and used on Linux-like systems, including MacOS and the Linux subsystem for Windows.

Required software:
- CMake 3.15+
- C++17
- [SUNDIALS](https://computing.llnl.gov/projects/sundials)
    - CVODE and KINSOL

Optional software:
- [Doxygen](https://www.doxygen.nl/) (for building documentation)
- [graphviz](https://graphviz.org/download/) (for Doxygen)

## Build and installation instructions
1. Create and navigate into a top-level `build` directory
2. Configure CMake: `cmake ..`
3. Build: `make`
4. Install: `make install`

The build process installs the executable in `run/bones.x`.

## CMake configuration variables
The default CMake configuration should be adequate for users that do not immediately require the documentation. CMake configuration options can be set by editing the top-level `CMakeLists.txt` file, or specifying options on the command line during step 2 as follows:
```
cmake -DBUILD_DOCS=ON ..
```
Then build the documentation with `make docs`, and navigate to `docs/index.html` to view the documentation.

# Using Bones

Bones is called from the command line in the `run` directory. The code can be run with the following options:
- `./bones.x`
- `./bones.x pathTo/someInputFile.yaml`
In the first case, the code uses file `../input/input.yaml`.

# Examples


