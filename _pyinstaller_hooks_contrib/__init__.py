# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

import sys

__version__ = '2025.7'
__maintainer__ = 'Legorooj, bwoodsend'
__uri__ = 'https://github.com/pyinstaller/pyinstaller-hooks-contrib'


def get_hook_dirs():
    import os
    hooks_dir = os.path.dirname(__file__)
    return [
        # Required because standard hooks are in sub-directory instead of the top-level hooks directory.
        os.path.join(hooks_dir, 'stdhooks'),
        # pre_* and run-time hooks
        hooks_dir,
    ]


# Several packages for which provide hooks are involved in deep dependency chains when various optional dependencies are
# installed in the environment, and their analysis typically requires recursion limit that exceeds the default 1000.
# Therefore, automatically raise the recursion limit to at least 5000. This alleviates the need to do so on per-hook
# basis.
new_recursion_limit = 5000
if sys.getrecursionlimit() < new_recursion_limit:
    sys.setrecursionlimit(new_recursion_limit)
