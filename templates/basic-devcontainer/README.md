# How to compile
First of all, the devcontainer should be build and started. Either use vscode or:
```
devcontainer up --workspace-folder .
```

Then start a bash in the devcontainer:
```
devcontainer exec --workspace-folder . bash
```
and in that bash execute:
```
rm -rf build &&
conan install --output-folder build {{profile}} --build=missing -s build_type=Debug . &&
conan install --output-folder build {{profile}} --build=missing -s build_type=Release . &&
cmake --workflow --preset=ctAll
```
## How to execute (inside the devcontainer's bash)
```
build/Debug/{{name}}
```
or
```
build/Release/{{name}}
```
