#-----------------------------------------------------------------------------
# Copyright (c) 2021, PyInstaller Development Team.
#
# This file is distributed under the terms of the Apache License 2.0
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: Apache-2.0
#-----------------------------------------------------------------------------

def _pyi_rthook():
    import pygraphviz

    # Override pygraphviz.AGraph._which method to search for graphviz executables inside sys._MEIPASS
    if hasattr(pygraphviz.AGraph, '_which'):

        def _pygraphviz_override_which(self, name):
            import os
            import sys
            import platform

            program_name = name
            if platform.system() == "Windows":
                program_name += ".exe"

            # First, check pygraphviz/bin directory (used by pygraphviz >= 2.0 PyPI wheels to bundle executables).
            program_path = os.path.join(sys._MEIPASS, 'pygraphviz', 'bin', program_name)
            if os.path.isfile(program_path):
                return program_path

            # Try top-level application directory
            program_path = os.path.join(sys._MEIPASS, program_name)
            if os.path.isfile(program_path):
                return program_path

            # Not found - instead of falling back to system copy, raise an error
            raise ValueError(f"Prog {name} not found in the PyInstaller-frozen application bundle!")

        pygraphviz.AGraph._which = _pygraphviz_override_which


_pyi_rthook()
del _pyi_rthook
