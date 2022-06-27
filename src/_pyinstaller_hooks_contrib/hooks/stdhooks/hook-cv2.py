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

import glob
import os
import pathlib

from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files, get_module_file_attribute
from PyInstaller import compat

hiddenimports = ['numpy']

# On Windows, make sure that opencv_videoio_ffmpeg*.dll is bundled
binaries = []
if compat.is_win:
    # If conda is active, look for the DLL in its library path
    if compat.is_conda:
        libdir = os.path.join(compat.base_prefix, 'Library', 'bin')
        pattern = os.path.join(libdir, 'opencv_videoio_ffmpeg*.dll')
        for f in glob.glob(pattern):
            binaries.append((f, '.'))

    # Include any DLLs from site-packages/cv2 (opencv_videoio_ffmpeg*.dll
    # can be found there in the PyPI version)
    binaries += collect_dynamic_libs('cv2')

# OpenCV loader from 4.5.4.60 requires extra config files and modules
datas = collect_data_files('cv2', include_py_files=True, includes=['**/*.py'])

# In linux PyPI opencv-python wheels, the cv2 extension is linked against Qt, and the wheel bundles a basic subset of Qt
# shared libraries, plugins, and font files. This is not the case on other OSes (presumably native UI APIs are used by
# OpenCV HighGUI module), nor in the headless PyPI wheels (opencv-python-headless).
# The bundled Qt shared libraries should be picked up automatically due to binary dependency analysis, but we need to
# collect plugins and font files from the `qt` subdirectory.
if compat.is_linux:
    pkg_path = pathlib.Path(get_module_file_attribute('cv2')).parent
    # Collect .ttf files fron fonts directory.
    # NOTE: since we are using glob, we can skip checks for (sub)directories' existence.
    qt_fonts_dir = pkg_path / 'qt' / 'fonts'
    datas += [
        (str(font_file), str(font_file.parent.relative_to(pkg_path.parent)))
        for font_file in qt_fonts_dir.rglob('*.ttf')
    ]
    # Collect .so files from plugins directory.
    qt_plugins_dir = pkg_path / 'qt' / 'plugins'
    binaries += [
        (str(plugin_file), str(plugin_file.parent.relative_to(pkg_path.parent)))
        for plugin_file in qt_plugins_dir.rglob('*.so')
    ]
