# ------------------------------------------------------------------
# Copyright (c) 2021 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------
"""
Spacy contains hidden imports and data files which are needed to import it
"""

import sys

from PyInstaller.utils.hooks import collect_data_files, collect_submodules, logger

datas = collect_data_files("spacy")
hiddenimports = collect_submodules("spacy")

# Automatically raise recursion limit to ensure it is at least 5000; this attempts to mitigate recursion limit errors
# caused by some import chains that involve spacy, but also depend on the build environment (i.e., other packages
# installed in it).
new_limit = 5000
if sys.getrecursionlimit() < new_limit:
    logger.info("hook-spacy: raising recursion limit to %d", new_limit)
    sys.setrecursionlimit(new_limit)
