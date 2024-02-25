# CPP Tools

Some random ideas about helper tools to ease developing in C++.

## ct_create_project.py

Creates a C++ project using Conan 2 and CMake.
Just a hello world that uses the Boost libraries.
It also initializes the created directory with Git.

### Usage examples

To create a subdir "hello_world" with a complete C++ project that uses Conan and CMake:
```
ct_create_project.py hello_world
```
Read the created REAME.md file to inderstand how to compile it.

```
ct_create_project.py -h
```
Shows different options for executing ct_create_project.py.
