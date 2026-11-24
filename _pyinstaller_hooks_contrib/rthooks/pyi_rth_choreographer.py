#-----------------------------------------------------------------------------
# Copyright (c) 2026, PyInstaller Development Team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: Apache-2.0
#-----------------------------------------------------------------------------


def _pyi_rthook():
    import os
    import sys

    wrapper_path = os.path.join('choreographer', 'browsers', '_unix_pipe_chromium_wrapper.py')
    if len(sys.argv) >= 2 and sys.argv[1].endswith(wrapper_path):
        # Remove sys.executable from argv
        if sys.argv[0] == sys.executable:
            sys.argv = sys.argv[1:]

        # Run the wrapper by importing it as a module. (This import also ensures that the wrapper is, in fact, collected
        # as a module, as run-time hooks are subject to PyInstaller's import analysis.)
        import choreographer.browsers._unix_pipe_chromium_wrapper  # noqa: F401
        raise SystemExit(0)


_pyi_rthook()
del _pyi_rthook
