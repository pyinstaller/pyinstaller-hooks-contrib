# ------------------------------------------------------------------
# Copyright (c) 2021 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

# Python wrapper for pyshark(https://pypi.org/project/pyshark/)
# Tested with version 0.4.5


from PyInstaller.utils.hooks import collect_data_files

hiddenimports = ['pyshark', 'py._path.local', 'py._vendored_packages.iniconfig', 'pyshark.config']

datas = collect_data_files('pyshark')
