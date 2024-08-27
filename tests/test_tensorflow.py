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

from PyInstaller import isolated
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


# Test that if GPU is available in unfrozen python, it is also available in the frozen application. This aims to ensure
# that CUDA is properly collected on platforms where it is supported.
def test_tensorflow_gpu_available(pyi_builder):
    # Check that GPU is available
    @isolated.decorate
    def _check_gpu():
        import tensorflow as tf
        gpu_devices = tf.config.list_physical_devices('GPU')
        return bool(gpu_devices)

    if not _check_gpu():
        pytest.skip(reason="No GPU available.")

    pyi_builder.test_source(
        """
        import tensorflow as tf
        gpu_devices = tf.config.list_physical_devices('GPU')
        print(f"GPU devices: {gpu_devices!r}")
        if not gpu_devices:
            raise Exception("No GPU available!")
        """
    )
