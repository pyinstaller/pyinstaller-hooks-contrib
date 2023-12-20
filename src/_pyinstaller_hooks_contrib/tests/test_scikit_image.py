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

import pytest

from PyInstaller.utils.hooks import is_module_satisfies
from PyInstaller.utils.tests import importorskip


# Run the tests in onedir mode only
onedir_only = pytest.mark.parametrize('pyi_builder', ['onedir'], indirect=True)


# Basic import tests for sub-packages of skimage. Run only on demand, and only in onedir mode.
@pytest.mark.slow
@onedir_only
@importorskip('skimage')
@pytest.mark.skipif(
    not is_module_satisfies('scikit_image >= 0.16'),
    reason='The test supports only scikit-image >= 0.16.',
)
@pytest.mark.parametrize('submodule', [
    'color', 'data', 'draw', 'exposure', 'feature', 'filters', 'future',
    'graph', 'io', 'measure', 'metrics', 'morphology', 'registration',
    'restoration', 'segmentation', 'transform', 'util'
])
def test_skimage(pyi_builder, submodule):
    pyi_builder.test_source("""
        import skimage.{0}
        """.format(submodule))
