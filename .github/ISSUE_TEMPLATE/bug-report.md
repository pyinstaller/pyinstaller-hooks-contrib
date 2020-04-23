---
name: Bug Report
about: Is there a bug in a hook?
title: ''
labels: state:triage
assignees: ''

---

**Describe the bug**
* Which hook/library isn't working? 
* Does the error get raised while building or when running?

**To Reproduce**

A minimal example file:
```
from foo import bar
bar.do_something()
```

PyInstaller command:
```
pyinstall test.py
```

Error:
```
Traceback (most recent call last):
  File "path/to/test.py", line XX, in <module>
   ...
SomeTypeOfError: Something went wrong
```

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. Windows/Ubuntu]
 - Python Version: [e.g. python 3.7]
 - Version of `pyinstaller-hooks-contrib`: [e.g. 2020.4]
 - Version of PyInstaller [e.g. 4.0]

**Additional context**
Add any other context about the problem here.
