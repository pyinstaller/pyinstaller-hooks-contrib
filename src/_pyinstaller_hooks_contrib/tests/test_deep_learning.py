# ------------------------------------------------------------------
# Copyright (c) 2023 PyInstaller Development Team.
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

from PyInstaller.utils.tests import importorskip


# Run the tests in onedir mode only
onedir_only = pytest.mark.parametrize('pyi_builder', ['onedir'], indirect=True)


# Basic transformers test with BERT-based unmasker
@importorskip('transformers')
@importorskip('torch')
@onedir_only
def test_transformers_bert_pipeline(pyi_builder):
    pyi_builder.test_source("""
        import transformers
        unmasker = transformers.pipeline('fill-mask', model='bert-base-uncased')
        output = unmasker("Hello I'm a [MASK] model.")
        print("Unmasked text:", output)
    """)


# Trying to import DebertaModel triggers error about missing source files for TorchScript
@importorskip('transformers')
@importorskip('torch')
@onedir_only
def test_transformers_deberta_import(pyi_builder):
    pyi_builder.test_source("""
        from transformers import DebertaConfig, DebertaModel

        configuration = DebertaConfig()
        model = DebertaModel(configuration)
    """)
