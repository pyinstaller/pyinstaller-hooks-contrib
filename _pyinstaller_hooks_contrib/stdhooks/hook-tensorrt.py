# ------------------------------------------------------------------
# Copyright (c) 2026 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

import os
import sys
from pathlib import Path

from PyInstaller.log import logger as LOGGER

try:
    import tensorrt_libs
except Exception as e:  # pragma: no cover
    tensorrt_libs = None
    LOGGER.warning("Failed to import tensorrt_libs for hook: %r", e)

hiddenimports = []
if tensorrt_libs is not None:
    # Ensure the runtime libraries package is collected even if user code imports only `tensorrt`.
    hiddenimports.append("tensorrt_libs")


def _collect_trt_runtime_binaries():
    if tensorrt_libs is None:
        return []

    trt_libs_path = Path(os.path.dirname(tensorrt_libs.__file__))
    if sys.platform == "win32":
        trt_libs = [(str(dll), ".") for dll in trt_libs_path.rglob("*.dll")]
        LOGGER.info("Found %d TensorRT runtime DLLs in %s", len(trt_libs), trt_libs_path)
        return trt_libs
    if sys.platform.startswith("linux"):
        trt_libs = [(str(so), ".") for so in trt_libs_path.rglob("*.so*")]
        LOGGER.info("Found %d TensorRT runtime .so files in %s", len(trt_libs), trt_libs_path)
        return trt_libs

    return []


binaries = _collect_trt_runtime_binaries()
