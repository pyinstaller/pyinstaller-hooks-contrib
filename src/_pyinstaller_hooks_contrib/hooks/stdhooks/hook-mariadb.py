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


from PyInstaller.utils.hooks import get_pyextension_imports


# The MariaDB uses a .pyd file and uses import within its __init__.py
# I looked for similar hooks and found that pyodbc uses this function
# for the import.
hiddenimports = get_pyextension_imports('mariadb')
