# How to compile
```
rm -rf build &&
conan install --output-folder build --build=missing -s build_type=Debug . &&
conan install --output-folder build --build=missing -s build_type=Release . &&
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
