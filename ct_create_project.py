#!/usr/bin/env python3
# This will create a folder with the bare minimum for a C++ project
# that uses Conan 2 and CMake to create a Hello World executable

import argparse
import git
import os
import subprocess
from jinja2 import Environment, FileSystemLoader


def parse_arguments():
    parser = argparse.ArgumentParser(description="Create C++, CMake, Conan2 project")
    parser.add_argument("name", help="Executable that will be compiled")
    parser.add_argument("--dir", default=None, help="directory to create (default: value of 'name' parameter)")
    parser.add_argument("-f", "--force", action="store_true", help="overwrite existing directories and/or files")
    parser.add_argument("--std", type=str, default="23", help="C++ standard to use (default: '23')")
    parser.add_argument("--profile", type=str, default=None, help="Conan profile to use")
    parser.add_argument("--no-git", action="store_true", help="Do not initialize the directory with git")
    args = parser.parse_args()
    if not args.dir:
        args.dir = args.name
    return args


def create_directories(args):
    try:
        os.makedirs(args.dir + "/src", exist_ok=args.force)
    except FileExistsError:
        print(f'error: directory "{args.dir}" already exists. Use "-f" to overwrite it.')


def create_files(args, cmake_version):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    env = Environment(loader=FileSystemLoader(f"{dir_path}/templates/creation"))
    file_list = [
        "conanfile.txt",
        "CMakeLists.txt",
        "src/main.cpp",
        ".gitignore",
        "README.md",
    ]
    profile = ""
    if args.profile:
        profile = f" -pr:b {args.profile} -pr {args.profile}"
    for template_file in file_list:
        template = env.get_template(template_file)
        output = template.render(name=args.name, standard=args.std, cmake_version=cmake_version, profile=profile)
        with open(args.dir + f"/{template_file}", "w") as f:
            f.write(output)


def check_conan():
    try:
        conan = subprocess.Popen(["conan", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = conan.communicate()
        if conan.returncode != 0:
            print(f"conan returned error code {conan.returncode}:\n{error.decode()}")
        for line in out.decode().splitlines():
            if line.startswith("Conan version"):
                return True
    except FileNotFoundError:
        print("error: conan command not found")
    except Exception as e:
        print(f"error: unexpected error executing conan: {e}")
    return False


def check_cmake():
    try:
        cmake = subprocess.Popen(["cmake", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = cmake.communicate()
        if cmake.returncode != 0:
            print(f"cmake returned error code {cmake.returncode}:\n{error.decode()}")
        for line in out.decode().splitlines():
            if line.startswith("cmake version "):
                return line[14:]
    except FileNotFoundError:
        print("error: cmake command not found")
    except Exception as e:
        print(f"error: unexpected error executing cmake: {e}")
    return False


def git_init(args):
    try:
        repo = git.Repo.init(args.dir)
        repo.index.add(
            [
                "conanfile.txt",
                "CMakeLists.txt",
                "src/main.cpp",
                ".gitignore",
                "README.md",
            ]
        )
        repo.index.commit("Initial commit")
    except git.GitCommandError as e:
        print(f"error initializing Git repository: {e}")


def main():
    args = parse_arguments()
    if not check_conan():
        return
    cmake_version = check_cmake()
    if not cmake_version:
        return
    create_directories(args)
    create_files(args, cmake_version)
    if not args.no_git:
        git_init(args)


if __name__ == "__main__":
    main()
