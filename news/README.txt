===========================================
PyInstaller-hooks-contrib changelog entries
===========================================

When contributing to PyInstaller-hooks-contrib, you'll need to add a changelog for most additions.


Entry types
-----------

There are 4 types of changelog entry:

* "new"
* "update"
* "process"
* "tests"


Use for each type
+++++++++++++++++

* Please use the "new" and "update" types for new or updated hooks respectively.

* The "process" type is for anything that doesn't fall into the other categories, but needs a changelog entry.

* The "tests" type is for edits to *just* the tests and nothing else. If you're adding/updating a new hook,
  and including tests, don't add two changelog entries! Only add this if it's a majorish *standalone*
  change to the tests.


Example
+++++++

You've added a hook for the module `foobar`, and it's in PR "9480".
You add the following file into the "news" directory, called "9480.new.rst".

    Add a hook for ``foobar``, which has a hidden import.

Done! The changelog entry has been added, and your PR is ready for review.


Test Suite
-----------

To run the test suite, install dependencies in root:
* pip install -r requirements-test.txt
* pip3 install -e .

Then run the test suite in root:
* If using Windows, run: `python -m PyInstaller.utils.run_tests`
* If using Linux, run: `python3 -m PyInstaller.utils.run_tests`
