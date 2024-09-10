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

from PyInstaller.utils.hooks import is_module_satisfies, collect_data_files

hiddenimports = []
datas = []

# In pydicom 3.0.0, the `pydicom.encoders` plugins were renamed to `pydicom.pixels.encoders`, and
# `pydicom.pixels.decoders` were also added. We need to collect them all, because they are loaded during
# `pydicom` module initialization. We intentionally avoid using `collect_submodules` here, because that causes
# import of `pydicom` with logging framework initialized, which results in error tracebacks being logged for all plugins
# with missing libraries (see https://github.com/pydicom/pydicom/issues/2128).
if is_module_satisfies('pydicom >= 3.0.0'):
    hiddenimports += [
        "pydicom.pixels.decoders.gdcm",
        "pydicom.pixels.decoders.pylibjpeg",
        "pydicom.pixels.decoders.pillow",
        "pydicom.pixels.decoders.pyjpegls",
        "pydicom.pixels.decoders.rle",
        "pydicom.pixels.encoders.gdcm",
        "pydicom.pixels.encoders.pylibjpeg",
        "pydicom.pixels.encoders.native",
        "pydicom.pixels.encoders.pyjpegls",
    ]

    # With pydicom 3.0.0, initialization of `pydicom` (unnecessarily) imports `pydicom.examples`, which attempts to set
    # up several test datasets: https://github.com/pydicom/pydicom/blob/v3.0.0/src/pydicom/examples/__init__.py#L10-L24
    additional_data_patterns = [
        # `pydicom/data/urls.json` and `pydicom/data/hashes.json` are required for data files that need to be downloaded
        # at run-time. The lack of former results in run-time error, while the lack of latter results in warnings about
        # dataset download failure.
        'urls.json',
        'hashes.json',
        # Try to collect these from the package, to avoid having to download them at run-time. The `pydicom` searches
        # for these files via recursive glob (`pathlib.Path.rglob`) to allow them being in sub-directories (for example,
        # `test_files/dicomdirtests/DICOMDIR`); so let us also assume that there might be sub-directories involved.
        "test_files/**/CT_small.dcm",
        "test_files/**/DICOMDIR",
        "test_files/**/US1_J2KR.dcm",
        "test_files/**/MR_small.dcm",
        "test_files/**/no_meta.dcm",
        "test_files/**/MR-SIEMENS-DICOM-WithOverlays.dcm",
        "test_files/**/OBXXXX1A.dcm",
        "test_files/**/US1_UNCR.dcm",
        "test_files/**/rtdose.dcm",
        "test_files/**/rtplan.dcm",
        "test_files/**/rtstruct.dcm",
        "test_files/**/waveform_ecg.dcm",
        "test_files/**/color3d_jpeg_baseline.dcm",
    ]
else:
    hiddenimports += [
        "pydicom.encoders.gdcm",
        "pydicom.encoders.pylibjpeg",
        "pydicom.encoders.native",
    ]
    additional_data_patterns = []

# Collect data files from `pydicom.data`; charset files and palettes might be needed during processing, so always
# collect them. Some other data files became required in v3.0.0 - the corresponding patterns are set accordingly in
# `additional_data_patterns` in the above if/else block.
datas += collect_data_files(
    'pydicom.data',
    includes=[
        'charset_files/*',
        'palettes/*',
        *additional_data_patterns,
    ],
)
