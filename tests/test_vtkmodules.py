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

import pytest

from PyInstaller import isolated
from PyInstaller.utils.hooks import can_import_module
from PyInstaller.utils.tests import importorskip


# Run the tests in onedir mode only
pytestmark = pytest.mark.parametrize('pyi_builder', ['onedir'], indirect=True)


@isolated.decorate
def _list_all_vtkmodules_submodules():
    try:
        import vtkmodules
    except Exception:
        return []

    return sorted(list(vtkmodules.__all__))


# Basic import tests for sub-modules of vtkmodules. Run only on demand, and only in onedir mode.
@pytest.mark.slow
@importorskip('vtkmodules')
@pytest.mark.parametrize('submodule', _list_all_vtkmodules_submodules())
def test_vtkmodules(pyi_builder, submodule):
    modname = f"vtkmodules.{submodule}"
    if not can_import_module(modname):
        pytest.skip(f"Module '{modname}' cannot be imported.")
    pyi_builder.test_source(f"""
        import {modname}
        """)
