``pyinstaller-hooks-contrib``: The PyInstaller community hooks repository
=========================================================================

THIS REPO IS IN ALPHA DEVELOPMENT AND NOT READY FOR USE
-------------------------------------------------------

What happens when (your?) package doesn't work with PyInstaller? Say you have data files that you need at runtime? 
PyInstaller doesn't bundle those. Your package requires others which PyInstaller can't see? How do you fix that?

In summary, a “hook” file extends PyInstaller to adapt it to the special needs and methods used by a Python package.
The word “hook” is used for two kinds of files. A runtime hook helps the bootloader to launch an app, setting up the
enviroment. A package hook (there are several types of those) tells PyInstaller what to include in the final app -
such as the data files and (hidden) imports mentioned above.

This repository is a collection of hooks for many packages, and allows PyInstaller to work with these packages with no
extra configuration. 

Installation
------------

``pyinstaller-hooks-contrib`` can **not** (yet) be installed with pip::

    pip install pyinstaller-hooks-contrib

