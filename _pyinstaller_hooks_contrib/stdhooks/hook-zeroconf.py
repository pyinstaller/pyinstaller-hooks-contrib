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

from PyInstaller.utils.hooks import collect_submodules

# PyPI wheels for zeroconf are cythonized, which prevents PyInstaller's module
# graph from seeing the imports performed by the extension modules.
hiddenimports = collect_submodules('zeroconf')
