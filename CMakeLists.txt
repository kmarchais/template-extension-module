cmake_minimum_required(VERSION 3.15)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX VERSION ${SKBUILD_PROJECT_VERSION})

configure_file(
    "${CMAKE_SOURCE_DIR}/src/${PROJECT_NAME}/_version.py.in"
    "${CMAKE_SOURCE_DIR}/src/${PROJECT_NAME}/_version.py"
    @ONLY
)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE src/main.cpp)
install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})
