# `pyinstaller-hooks-contrib`: The PyInstaller community hooks repository



What happens when (your?) package doesn't work with PyInstaller? Say you have data files that you need at runtime?
PyInstaller doesn't bundle those. Your package requires others which PyInstaller can't see? How do you fix that?

In summary, a "hook" file extends PyInstaller to adapt it to the special needs and methods used by a Python package.
The word "hook" is used for two kinds of files. A runtime hook helps the bootloader to launch an app, setting up the
environment. A package hook (there are several types of those) tells PyInstaller what to include in the final app -
such as the data files and (hidden) imports mentioned above.

This repository is a collection of hooks for many packages, and allows PyInstaller to work with these packages
seamlessly.

## Installation

`pyinstaller-hooks-contrib` is automatically installed when you install PyInstaller, or can be installed with pip:

```commandline
pip install -U pyinstaller-hooks-contrib
```


## I can't see a hook for `a-package`

Either `a-package` works fine without a hook, or no-one has contributed hooks.
If you'd like to add a hook, or view information about hooks,
please see [the wiki](https://github.com/pyinstaller/pyinstaller-hooks-contrib/wiki).


## I want to help!

Please start by providing pull requests and helping solve issues.
Please read [news/README.txt](https://github.com/pyinstaller/pyinstaller-hooks-contrib/blob/master/news/README.txt) before submitting you pull request.
If you plan to contribute frequently or are interested in becoming a developer,
send an email to `legorooj@protonmail.com` to let us know.

