# ------------------------------------------------------------------
# Copyright (c) 2024 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import collect_data_files, copy_metadata

# Collect default icon from `resources`.
datas = collect_data_files('toga_gtk')

# Collect metadata so that the backend can be discovered via `toga.backends` entry-point.
datas += copy_metadata("toga-gtk")

# Starting with version 0.5.4, toga tries to determine the path to "resources" directory directly from the `__file__`
# attribute of the `resources` submodule of a given factory module, whereas previous versions used the `__file__`
# attribute of the factory module itself. Therefore, we now need a hidden import for the `resources` submodule, to
# ensure that it is collected and treated as a regular package (rather than a namespace one) at run-time.
hiddenimports = ['toga_gtk.resources']
