
add_executable(bones.x)
target_sources(bones.x PRIVATE driver.cc 
                             drg.cc 
                             streams.cc)

set_property(TARGET bones.x PROPERTY INSTALL_RPATH_USE_LINK_PATH TRUE)  # adds LC_RPATH to executable

find_library(SUNKIN  sundials_kinsol REQUIRED)
find_library(SUNCV   sundials_cvodes REQUIRED)
find_library(SUNCORE sundials_core   REQUIRED)
find_library(FMT     fmt             REQUIRED)
find_library(CANTERA cantera         REQUIRED)

target_include_directories(bones.x PRIVATE "$ENV{CANTERA_INCLUDE_PATH}")
target_include_directories(bones.x PRIVATE "$ENV{CONDA_PREFIX}/include")
target_link_libraries(bones.x ${CANTERA} ${SUNKIN} ${SUNCV} ${SUNCORE} ${FMT})

install(TARGETS bones.x DESTINATION "${PROJECT_SOURCE_DIR}/run")
