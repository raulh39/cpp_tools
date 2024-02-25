cmake_minimum_required(VERSION {{cmake_version}})
project({{name}} VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(Boost REQUIRED CONFIG)

add_executable({{name}} src/main.cpp)
set_property(TARGET {{name}} PROPERTY CXX_STANDARD {{standard}})
set_property(TARGET {{name}} PROPERTY CXX_EXTENSIONS OFF)
target_link_libraries({{name}} PUBLIC Boost::headers)
