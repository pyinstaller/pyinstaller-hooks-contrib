# ------------------------------------------------------------------
# Copyright (c) 2025 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import copy_metadata, is_module_satisfies

# Starting with narwhals 1.35.0, we need to collect metadata for `typing_extensions`.
datas = []
if is_module_satisfies("narwhals >= 1.35.0"):
    datas += copy_metadata("typing_extensions")
