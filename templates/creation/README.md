# How to compile
```
conan install . --output-folder=build --build=missing{{profile}}
cmake --preset=conan-debug
cmake --build --preset=conan-debug
```
# How to execute
```
build/{{name}}
```
