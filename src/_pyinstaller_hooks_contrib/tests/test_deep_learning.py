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


# Building models from tabular data example from https://docs.fast.ai/quick_start.html
@importorskip('fastai')
@onedir_only
def test_fastai_tabular_data(pyi_builder):
    pyi_builder.test_source("""
        from fastai.tabular.all import *

        path = untar_data(URLs.ADULT_SAMPLE)
        print(f"Dataset path: {path}")

        dls = TabularDataLoaders.from_csv(
            path/'adult.csv',
            path=path,
            y_names="salary",
            cat_names = [
                'workclass',
                'education',
                'marital-status',
                'occupation',
                'relationship',
                'race',
            ],
            cont_names = [
                'age',
                'fnlwgt',
                'education-num',
            ],
            procs = [
                Categorify,
                FillMissing,
                Normalize,
            ],
        )

        learn = tabular_learner(dls, metrics=accuracy)
        learn.fit_one_cycle(2)
        learn.show_results()
    """)


@importorskip('timm')
@onedir_only
def test_timm_model_creation(pyi_builder):
    pyi_builder.test_source("""
        import timm

        # List available models
        pretrained_models = timm.list_models(pretrained=True)
        print(f"Pre-trained models: {len(pretrained_models)}")
        assert len(pretrained_models) > 0

        # Create a model (non-trained version, to avoid downloading weights)
        model = timm.create_model("resnet50d", pretrained=False)
        print(model)
    """)


@importorskip('lightning')
@importorskip('torchvision')
@importorskip('torch')
@onedir_only
def test_lightning_mnist_autoencoder(pyi_builder):
    pyi_builder.test_source("""
        import os

        import torch
        import torchvision
        import lightning


        class LitAutoEncoder(lightning.LightningModule):
            def __init__(self):
                super().__init__()
                self.encoder = torch.nn.Sequential(
                    torch.nn.Linear(28 * 28, 128),
                    torch.nn.ReLU(),
                    torch.nn.Linear(128, 3),
                )
                self.decoder = torch.nn.Sequential(
                    torch.nn.Linear(3, 128),
                    torch.nn.ReLU(),
                    torch.nn.Linear(128, 28 * 28),
                )

            def forward(self, x):
                embedding = self.encoder(x)
                return embedding

            def training_step(self, batch, batch_idx):
                x, y = batch
                x = x.view(x.size(0), -1)
                z = self.encoder(x)
                x_hat = self.decoder(z)
                loss = torch.nn.functional.mse_loss(x_hat, x)
                return loss

            def configure_optimizers(self):
                optimizer = torch.optim.Adam(
                    self.parameters(),
                    lr=1e-3,
                )
                return optimizer


        # Dataset
        dataset = torchvision.datasets.MNIST(
            os.path.dirname(__file__),
            download=True,
            transform=torchvision.transforms.ToTensor(),
        )
        dataset_size = len(dataset)
        num_samples = 100
        train, val = torch.utils.data.random_split(
            dataset,
            [num_samples, dataset_size - num_samples],
        )

        # Train
        autoencoder = LitAutoEncoder()
        trainer = lightning.Trainer(max_epochs=1, logger=False)
        trainer.fit(
            autoencoder,
            torch.utils.data.DataLoader(train),
        )
    """)
