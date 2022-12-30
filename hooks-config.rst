===========================
Supported hooks and options
===========================

This section lists hooks that are configurable in `pyinstaller-hooks-contrib`.

See also `Hook Configuration Options <https://pyinstaller.org/en/stable/hooks-config.html>`_
for more information regarding hook options - how to add new hook options,
hook options from primary pyinstaller repo, etc.


easyocr hook
------------

easyocr hook allows configuration of included language-related data files
(there are a number of text files with characters and dictionaries per language).
Dictionaries are quite large (about 290MB at the time of writing),
so it's likely that end-users would want to only include what they use.

If not set to languages used, an error in `setLanguageList()` will occur at runtime::

   No such file or directory: '<PATH>/easyocr/character/<LANG_CODE>_char.txt'


**Hook identifier:** ``easyocr``

**Options**

 * ``lang_codes`` [*list of strings*]: list of ISO 639 language code (e.g., ``en``) for
   which data files should be collected.
   By default, all languages will be included (``*`` in place of the language code).

**Example**

Collect only data files required for English, French and Spanish::

    a = Analysis(
        ['my-ocr-app.py'],
        ...,
        hooksconfig={
            'easyocr': {
                'lang_codes': ['en', 'fr', 'es'],
            },
        },
        ...,
    )


.. Emacs config:
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
