import os
import platform
import struct
import pathlib
from ctypes import util
from PyInstaller.utils.hooks import get_module_file_attribute, logger

"""
Hook for pylsl, i.e., the Python wrapper around labstreaminglayer (aka LSL).
The pylsl package loads the C++ liblsl library using CDLL. The logic for
locating liblsl is replicated here; subsequently it is added to the binaries
and packaged in the compiled version such that pylsl will be able to find it
there as well.

See also
-  https://labstreaminglayer.readthedocs.io
-  https://github.com/labstreaminglayer/pylsl
-  https://github.com/sccn/liblsl
"""


def find_liblsl_library():
    """finds the binary lsl library.

    Search order is to first try to use the path stored in the environment
    variable PYLSL_LIB (if available), then search through the package
    directory, and finally search the whole system.
    """

    # first try the environment variable PYLSL_LIB
    if "PYLSL_LIB" in os.environ:
        libfile = os.environ["PYLSL_LIB"]
        if libfile and os.path.isfile(libfile):
            return libfile

    # this will only run if PYLSL_LIB did not resolve the library
    os_name = platform.system()
    if os_name in ["Windows", "Microsoft"]:
        libsuffix = ".dll"
    elif os_name == "Darwin":
        libsuffix = ".dylib"
    elif os_name == "Linux":
        libsuffix = ".so"
    else:
        raise RuntimeError("unrecognized operating system:", os_name)

    for scope in ["package", "system"]:
        for libprefix in ["", "lib"]:
            for debugsuffix in ["", "-debug"]:
                for bitness in ["", str(8 * struct.calcsize("P"))]:
                    if scope == "package":
                        # try in the package directory at pylsl/lib
                        module_dir = pathlib.Path(get_module_file_attribute('pylsl')).parent
                        libfile = os.path.join(module_dir, libprefix + "lsl" + bitness + debugsuffix + libsuffix)
                        if libfile and os.path.isfile(libfile):
                            return libfile
                    elif (scope == "system") and os_name not in ["Windows", "Microsoft"]:
                        # try on the system library path, this includes the conda library path
                        libfile = util.find_library(libprefix + "lsl" + bitness + debugsuffix)
                        if libfile and os.path.isfile(libfile):
                            return libfile
                    elif (scope == "system") and os_name == "Darwin":
                        # try on the homebrew library path
                        libfile = util.find_library('/opt/homebrew/lib/' + libprefix + "lsl" + bitness + debugsuffix)
                        if libfile and os.path.isfile(libfile):
                            return libfile
    

libfile = find_liblsl_library()

if libfile:
    # add the liblsl library to the binaries
    # it gets packaged in pylsl/lib, which is where pylsl will look first
    binaries = [(libfile, os.path.join('pylsl', 'lib'))]
else:
    logger.warning("liblsl shared library not found - pylsl will likely fail to work!")
    binaries = []


if __name__ == '__main__':
    print(binaries)
