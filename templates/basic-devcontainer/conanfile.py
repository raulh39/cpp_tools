from conan import ConanFile
from conan.tools.cmake import CMakeToolchain

class Pkg(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    def requirements(self):
        # self.requires("boost/1.84.0")
        pass

    def build_requirements(self):
        pass

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()
