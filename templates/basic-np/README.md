# How to compile
```
rm -rf build &&
conan install --output-folder build {{profile}} --build=missing -s build_type=Debug . &&
conan install --output-folder build {{profile}} --build=missing -s build_type=Release . &&
cmake --workflow --preset=ctAll
```
## How to execute
```
build/Debug/{{name}}
```
or
```
build/Release/{{name}}
```
