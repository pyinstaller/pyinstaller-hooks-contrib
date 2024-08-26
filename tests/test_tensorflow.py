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

import pytest

from PyInstaller.utils.tests import importorskip


pytestmark = [
    importorskip('tensorflow'),
    # Run the tests in onedir mode only
    pytest.mark.parametrize('pyi_builder', ['onedir'], indirect=True)
]


def test_tensorflow(pyi_builder):
    pyi_builder.test_source(
        """
        from tensorflow import *
        """
    )


# Test if tensorflow.keras imports properly result in tensorflow being collected.
# See https://github.com/pyinstaller/pyinstaller/discussions/6890
def test_tensorflow_keras_import(pyi_builder):
    pyi_builder.test_source(
        """
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense, LSTM, Dropout
        from tensorflow.keras.optimizers import Adam
        """
    )


def test_tensorflow_layer(pyi_builder):
    pyi_builder.test_script('pyi_lib_tensorflow_layer.py')


def test_tensorflow_mnist(pyi_builder):
    pyi_builder.test_script('pyi_lib_tensorflow_mnist.py')
