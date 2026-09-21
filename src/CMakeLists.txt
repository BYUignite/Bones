
add_executable(drg.x)
target_sources(drg.x PRIVATE driver.cc 
                             drg.cc 
                             streams.cc)

set_property(TARGET drg.x PROPERTY INSTALL_RPATH_USE_LINK_PATH TRUE)  # adds LC_RPATH to executable

find_library(SUNKIN  sundials_kinsol REQUIRED)
find_library(SUNCV   sundials_cvodes REQUIRED)
find_library(SUNCORE sundials_core   REQUIRED)
find_library(FMT     fmt             REQUIRED)
find_library(CANTERA cantera         REQUIRED)

target_include_directories(drg.x PRIVATE "$ENV{CANTERA_INCLUDE_PATH}")
target_include_directories(drg.x PRIVATE "$ENV{CONDA_PREFIX}/include")
target_link_libraries(drg.x ${CANTERA} ${SUNKIN} ${SUNCV} ${SUNCORE} ${FMT})

install(TARGETS drg.x DESTINATION "${PROJECT_SOURCE_DIR}/run")
