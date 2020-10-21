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


"""
Hook for PyZMQ. Cython based Python bindings for messaging library ZeroMQ.
http://www.zeromq.org/
"""
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = ['zmq.utils.garbage']

# PyZMQ comes with two backends, cython and cffi. Calling collect_submodules()
# on zmq.backend seems to trigger attempt at compilation of C extension
# module for cffi backend, which will fail if ZeroMQ development files
# are not installed on the system. On non-English locales, the resulting
# localized error messages may cause UnicodeDecodeError. Collecting each
# backend individually, however, does not seem to cause any problems.
hiddenimports += ['zmq.backend']

hiddenimports += collect_submodules('zmq.backend.cython')
hiddenimports += collect_submodules('zmq.backend.cffi')
