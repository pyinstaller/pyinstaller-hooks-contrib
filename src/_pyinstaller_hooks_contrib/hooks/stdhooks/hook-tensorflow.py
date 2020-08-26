# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import is_module_satisfies, \
    collect_submodules, collect_data_files

if is_module_satisfies("tensorflow < 1.15.0"):
    # 1.14.x and earlier: collect everything from tensorflow
    hiddenimports = collect_submodules('tensorflow')
    datas = collect_data_files('tensorflow')
elif is_module_satisfies("tensorflow >= 1.15.0") and is_module_satisfies("tensorflow < 2.2.0"):
    # 1.15.x - 2.1.x: collect everything from tensorflow_core
    hiddenimports = collect_submodules('tensorflow_core')
    datas = collect_data_files('tensorflow_core')

    # Under 1.15.x, we seem to fail collecting a specific submodule,
    # and need to add it manually...
    if is_module_satisfies("tensorflow >= 1.15.0") and is_module_satisfies("tensorflow < 2.0.0"):
        hiddenimports += ['tensorflow_core._api.v1.compat.v2.summary.experimental']
else:
    # 2.2.0 and newer: collect everything from tensorflow again
    hiddenimports = collect_submodules('tensorflow')
    datas = collect_data_files('tensorflow')
