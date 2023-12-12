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

from PyInstaller.utils.tests import importorskip


def torch_onedir_only(test):

    def wrapped(pyi_builder):
        if pyi_builder._mode != 'onedir':
            pytest.skip('PyTorch tests support only onedir mode due to potential distribution size.')
        test(pyi_builder)

    return wrapped


@importorskip('torch')
@torch_onedir_only
def test_torch(pyi_builder):
    pyi_builder.test_source("""
        import torch

        torch.rand((10, 10)) * torch.rand((10, 10))
    """)


@importorskip('torchvision')
@torch_onedir_only
def test_torchvision_nms(pyi_builder):
    pyi_builder.test_source("""
        import torch
        import torchvision
        # boxes: Nx4 tensor (x1, y1, x2, y2)
        boxes = torch.tensor([
            [0.0, 0.0, 1.0, 1.0],
            [0.45, 0.0, 1.0, 1.0],
        ])
        # scores: Nx1 tensor
        scores = torch.tensor([
            1.0,
            1.1
        ])
        keep = torchvision.ops.nms(boxes, scores, 0.5)
        # The boxes have IoU of 0.55, and the second one has a slightly
        # higher score, so we expect it to be kept while the first one
        # is discarded.
        assert keep == 1
    """)
