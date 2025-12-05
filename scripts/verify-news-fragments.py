#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# Copyright (c) 2013-2021, PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
#-----------------------------------------------------------------------------
"""
Verify that new news entries have valid filenames. Usage:

.. code-block:: bash

    python scripts/verify-news-fragments.py

"""

import re
import sys
from pathlib import Path

CHANGELOG_GUIDE = \
    "https://github.com/pyinstaller/pyinstaller-hooks-contrib/tree/master/news#readme"

CHANGE_TYPES = {
    'new', 'update', 'remove', 'process', 'tests', 'breaking'
}

NEWS_PATTERN = re.compile(r"(\d+)\.(\w+)\.(?:(\d+)\.)?rst")

NEWS_DIR = Path(__file__).absolute().parent.parent / "news"


def validate_name(name):
    """
    Check a filename/filepath matches the required format.

    :param name: Name of news fragment file.
    :type: str, os.Pathlike

    :raises: ``SystemExit`` if above checks don't pass.
    """
    match = NEWS_PATTERN.fullmatch(Path(name).name)
    if match is None:
        raise SystemExit(
            f"'{name}' does not match the '(pr-number).(type).rst' or '(pr-number).(type).(enumeration).rst' changelog "
            f"entries formats. See:\n{CHANGELOG_GUIDE}"
        )

    if match.group(2) not in CHANGE_TYPES:
        sys.exit("'{}' is of invalid type '{}'. Valid types are: {}".format(name, match.group(2), CHANGE_TYPES))

    print(name, "is ok")


def main():

    for file in NEWS_DIR.iterdir():
        if file.name in ("README.txt",  "_template.rst"):
            continue
        validate_name(file.name)

    # Ensure that news items aren't left in the repo's root.
    for file in NEWS_DIR.parent.iterdir():
        if NEWS_PATTERN.match(file.name):
            raise SystemExit("{file} is in the wrong directory. It should be moved to the 'news' directory.")


if __name__ == "__main__":
    main()
