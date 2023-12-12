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


# Run the tests in onedir mode only
torch_onedir_only = pytest.mark.parametrize('pyi_builder', ['onedir'], indirect=True)


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


# Advanced tests that uses torchvision.datasets and torchvision.transforms;
# the transforms are combined using torchscript, which requires access to
# transforms' sources.
@importorskip('torchvision')
@torch_onedir_only
def test_torchvision_scripted_transforms(pyi_builder):
    pyi_builder.test_source("""
        import torch
        import torch.nn

        import torchvision.transforms
        import torchvision.datasets

        # Generate one image, and convert it from PIL to tensor
        preproc = torchvision.transforms.Compose([
            torchvision.transforms.PILToTensor()
        ])

        dataset = torchvision.datasets.FakeData(
            size=1,  # 1 image
            image_size=(3, 200, 200),
            num_classes=2,
            transform=preproc,
        )

        assert len(dataset) == 1
        image, category = dataset[0]

        assert image.size() == (3, 200, 200)
        assert image.dtype == torch.uint8

        # Create a composite transform that uses torchscript
        transforms = torch.nn.Sequential(
            torchvision.transforms.RandomCrop(100),
            torchvision.transforms.RandomHorizontalFlip(p=0.3),
        )
        scripted_transforms = torch.jit.script(transforms)

        # Transform image
        transformed_image = scripted_transforms(image)

        assert transformed_image.size() == (3, 100, 100)
        assert transformed_image.dtype == torch.uint8
    """)
