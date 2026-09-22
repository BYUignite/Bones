################### PREAMBLE

cmake_minimum_required(VERSION 3.15)

project(drg LANGUAGES CXX)

################### PROJECT SETUP

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)       # Release or Debug
endif()

# ---- set C++ language standard ----

set(CMAKE_VERBOSE_MAKEFILE ON)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)

# ---- build options ----

option(BUILD_DOCS "Build documentation" ON)

################### MAIN PROJECT TARGETS

add_subdirectory(src)

################### OPTIONAL PROJECT TARGETS

#-------- DOCUMENTATION --------

if(BUILD_DOCS)
    add_subdirectory(docs)
endif()

