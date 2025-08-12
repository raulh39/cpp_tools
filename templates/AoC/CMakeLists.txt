cmake_minimum_required(VERSION {{cmake_version}})
project({{name}} VERSION 0.1.0 LANGUAGES CXX)

# find_package(Boost REQUIRED CONFIG)

add_executable(part1)
target_sources(part1 PUBLIC src/part1.cpp)
