# How to compile
```
mkdir build

cmake -B build -S . \
-DCMAKE_PROJECT_TOP_LEVEL_INCLUDES=conan_provider.cmake \
-DCMAKE_BUILD_TYPE=Debug \
-DCMAKE_EXPORT_COMPILE_COMMANDS=ON

cmake --build build --config Debug
```
# How to execute
```
build/{{name}}
```
