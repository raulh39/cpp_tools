cmake_minimum_required(VERSION {{cmake_version}})
project({{name}} VERSION 0.1.0 LANGUAGES CXX)

find_package(Boost REQUIRED CONFIG)

add_executable({{name}} src/main.cpp)
target_link_libraries({{name}} PUBLIC Boost::headers)
