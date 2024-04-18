#-----------------------------------------------------------------------------
# Copyright (c) 2024, PyInstaller Development Team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: Apache-2.0
#-----------------------------------------------------------------------------

import os
import sys

# If we collected OpenSSL modules into `ossl-modules` directory, override the OpenSSL search path by setting the
# `OPENSSL_MODULES` environment variable.
_ossl_modules_dir = os.path.join(sys._MEIPASS, 'ossl-modules')
if os.path.isdir(_ossl_modules_dir):
    os.environ['OPENSSL_MODULES'] = _ossl_modules_dir
del _ossl_modules_dir
