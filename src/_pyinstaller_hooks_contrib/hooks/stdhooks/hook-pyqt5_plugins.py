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

from PyInstaller.utils.hooks import copy_metadata, collect_submodules
# Those modules uses pkg_resources.get_distribution(foo()) which are not detectable via bytecode scanning
datas = [copy_metadata("pyqt5_plugins"), copy_metadata("qt5_tools"), copy_metadata("qt5_applications")]
# Lazily loaded submodules ( importlib.import_module() )
hiddenimports = ["qt5_tools", collect_submodules("pyqt5_plugins"), collect_submodules("qt5_applications")]
