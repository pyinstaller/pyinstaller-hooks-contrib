# ------------------------------------------------------------------
# Copyright (c) 2023 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

import os

from PyInstaller.utils.hooks import (
    logger,
    is_module_satisfies,
)


# Helper for collecting shared libraries from NVIDIA CUDA packages on linux.
def collect_nvidia_cuda_binaries(hook_file):
    # Find the module underlying this nvidia.something hook; i.e., change ``/path/to/hook-nvidia.something.py`` to
    # ``nvidia.something``.
    hook_name, hook_ext = os.path.splitext(os.path.basename(hook_file))
    assert hook_ext.startswith('.py')
    assert hook_name.startswith('hook-')
    module_name = hook_name[5:]

    # `search_patterns` was added to `collect_dynamic_libs` in PyInstaller 5.8, so that is the minimum required version.
    binaries = []
    if is_module_satisfies('PyInstaller >= 5.8'):
        from PyInstaller.utils.hooks import collect_dynamic_libs, PY_DYLIB_PATTERNS
        binaries = collect_dynamic_libs(
            module_name,
            # Collect fully-versioned .so files (not included in default search patterns).
            search_patterns=PY_DYLIB_PATTERNS + ["lib*.so.*"],
        )
    else:
        logger.warning("hook-%s: this hook requires PyInstaller >= 5.8!", module_name)

    return binaries
