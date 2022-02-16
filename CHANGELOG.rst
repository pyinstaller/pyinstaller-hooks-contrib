

Updated hooks
~~~~~~~~~~~~~

* Fix hook for ``azurerm`` when ``pyinstaller >= 4.4"``. (`#283
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/283>`_)
* Fix hook for astropy when astropy >= 5.0. (`#381
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/381>`_)


New hooks
~~~~~~~~~

* Add a hook for ``py`` which has dynamically loaded vendored submodules.
  This fixes compatibility with ``pytest >= 7.0.0``. (`#376
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/376>`_)
* Added a hook for ``orjson``, which has hidden imports. (`#378
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/378>`_)


2022.0 (2022-01-24)

New hooks
~~~~~~~~~

* Add a hook for ``pypsexec``, which has a data files. (`#366
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/366>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``tensorflow``  hook to add support for ``tensorflow`` 2.6.x and
  later. (`#371
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/371>`_)


Test-suite and Continuous Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Add a test for ``mimesis`` hook. (`#367
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/367>`_)


2021.5 (2022-01-07)

New hooks
~~~~~~~~~

* Add a hook for ``mimesis``, which has a data files. (`#365
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/365>`_)


Updated hooks
~~~~~~~~~~~~~

* Add a runtime hook for ``pygraphviz`` that modifies the search behavior
  for ``graphviz`` programs, in order to ensure that the collected programs
  in ``sys._MEIPASS`` are found and used. (`#357
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/357>`_)


2021.4 (2021-11-29)

New hooks
~~~~~~~~~

* Add a hook for ``adbutils`` to collect dynamic libraries. (`#323
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/323>`_)
* Add a hook for ``branca`` to collect data files. (`#318
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/318>`_)
* Add a hook for ``dash`` to collect data files required by the new ``dash``
  v2.0. (`#314
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/314>`_)
* Add a hook for ``doc2xpdf`` to collect qss data files. (`#310
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/310>`_)
* Add a hook for ``ffpyplayer``. (`#348
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/348>`_)
* Add a hook for ``pyppeteer``. (`#329
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/329>`_)
* Add a hook for ``pyvjoy`` to collect dynamic libraries. (`#321
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/321>`_)
* Add a hook for ``qtmodern`` to collect qss data files. (`#305
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/305>`_)
* Add a hook for ``tableauhyperapi`` to collect dynamic libraries. (`#316
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/316>`_)
* Add a hook for ``websockets`` which lazily loads its submodules. (`#301
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/301>`_)
* Add hook for ``folium``. (`#62
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/62>`_)
* Add hook for ``metpy``. (`#60
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/60>`_)
* Add hook for ``panel``. (`#338
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/338>`_)
* Add hook for ``platformdirs``. This in turn fixes compatibility with ``pylint
  >= 2.10.2``. (`#301
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/301>`_)
* Add hook for ``pymediainfo``. (`#324
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/324>`_)
* Add hook for ``pyviz_comms``. (`#338
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/338>`_)
* Add hook for ``sacremoses``. (`#325
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/325>`_)
* Add hook for ``tzdata``. (`#339
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/339>`_)
* Add hooks for ``cairocffi`` and ``CairoSVG``. (`#347
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/347>`_)
* Add hooks for ``pyphen`` and ``kaleido``. (`#345
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/345>`_)
* Add hooks for ``zoneinfo`` and ``backports.zoneinfo``. (`#339
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/339>`_)


Updated hooks
~~~~~~~~~~~~~

* Removed the ``certifi`` run-time hook because it was not required for
  ``certifi`` to function in a frozen application. It was sometimes setting the
  ``SSL_CERT_FILE`` environment variable which causes applications to behave
  differently when frozen. In particular the
  ``SSLContext.set_default_verify_paths()`` method loads the certificates from
  ``certifi`` when the ``SSL_CERT_FILE`` environment variable is set. (`#335
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/335>`_)
* Update ``cv2`` hook to collect extra config files and modules for
  compatibility with OpenCV 4.5.4.60. (`#354
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/354>`_)
* Update ``markdown`` hook to include package metadata, enabling the use of
  short names for built-in extensions, such as ``extra`` or ``toc``. (`#336
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/336>`_)
* Update hiddenimports for ``APScheduler > 3.8.0``. (`#333
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/333>`_)
* Update hiddenimports for ``pymssql > 2.1.5``. (`#315
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/315>`_)


2021.3 (2021-08-25)

New hooks
~~~~~~~~~

* Add a hook for ``dash-uploader`` to collect data files (`#280
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/280>`_)
* Add a hook for ``langdetect`` to collect data files. (`#285
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/285>`_)
* Add a hook for ``mariadb`` to collect hidden imports. (`#279
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/279>`_)
* Add a hook for ``mnemonic`` to collect data files (`#284
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/284>`_)
* Add a hook for ``msoffcrypto`` to collect metadata. (`#139
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/139>`_)
* Add a hook for ``pingouin`` to collect data files. (`#292
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/292>`_)
* Add a hook for ``pystray`` to collect hidden imports. (`#288
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/288>`_)
* Add a hook for ``rtree`` to collect dynamic libraries. (`#291
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/291>`_)
* Add a hook for ``shotgun_api3`` to collect data files and hidden imports.
  (`#138
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/138>`_)
* Add a hook for ``swagger_spec_validator`` to collect data files. (`#296
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/296>`_)
* Add a hook for ``timezonefinder`` to collect data files. (`#294
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/294>`_)
* Add a hook for ``uvicorn`` to collect data files. (`#300
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/300>`_)
* Add a hook for `cloudscraper` to collect data files (`#281
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/281>`_)
* Add a hook for `pynput` to collect hidden imports. (`#287
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/287>`_)
* Added a standard hook for SunPy. (`#134
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/134>`_)
* Added hook to get data for the parso package (needed for IPython
  autocomplete) (`#275
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/275>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``clr`` hook to set the correct path for pythonnet 3.0 (`#295
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/295>`_)
* Update ``scikit-learn`` and ``scikit-image`` hooks to perform version checks
  based on distribution name instead of package name, to prevent failures
  when ``sklearn`` dummy distribution is installed. (`#276
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/276>`_)


2021.2 (2021-06-26)

New hooks
~~~~~~~~~

* Add a hook for ``Azurerm`` which is using pkg_resources internally. (`#123
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/123>`_)
* Add a hook for ``Office365-REST-Python-Client`` which uses data files in some
  methods (`#125
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/125>`_)
* Add a hook for ``spacy`` which contains hidden imports and data files (`#1
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/1>`_)
* Add a standard hook for PyPylon. (`#114
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/114>`_)
* Add hook for ``blspy`` that collects ``MPIR`` DLLs on Windows. (`#119
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/119>`_)
* Add hook for ``flirpy`` that collects data files on Windows. (`#120
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/120>`_)
* Add hook for ``jsonrpcserver`` to collect missing ``request-schema.json``
  data file. (`#126
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/126>`_)
* Add hook for ``plotly`` to collect data files and hidden `pandas`, `cmath`,
  and `plotly.validator` imports

  Add hooks for ``dash`` and related packages to collect data files and hook
  for meta-data from ``flask-compress``

  Add hook for ``dash_bootstrap_components`` to collect data files (`#103
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/103>`_)
* Add hook for ``pyttsx3`` whose drivers are hidden imports. (`#101
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/101>`_)
* Add hook for ``srsly.msgpack._packer`` which contains a hidden import (`#3
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/3>`_)
* Add hook for `humanize <https://pypi.org/project/humanize>`__ to include
  required metadata. (`#122
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/122>`_)
* Add hooks for ``thinc`` and ``thinc.banckends.numpy_ops`` which contain data
  files and hidden imports (`#2
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/2>`_)
* Added a hook for ``statsmodels``, which adds ``statsmodels.tsa.statespace``
  as a hidden import (`#100
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/100>`_)


Updated hooks
~~~~~~~~~~~~~

* (Windows) Update ``zmq`` hook for compatibility with new shared libraries
  location in Windows build of ``pyzmq`` 22.0.0 and later. (`#98
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/98>`_)
* Add ```googleapiclient.discovery``` json files to work with services
  like Blogger v3 on the ```build()``` method. (`#97
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/97>`_)
* Remove ``win32ctypes.core`` hook, as an improved copy is provided as part
  of main PyInstaller's hooks collection. (`#124
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/124>`_)
* Update ``scikit-image`` hooks for compatibility with 0.18.x series. (`#107
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/107>`_)
* Update ``scikit-learn`` hooks for compatibility with 0.24.x series. (`#108
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/108>`_)
* Update hook for PyPylon to include data files. (`#116
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/116>`_)
* Update the hook for ``pycountry`` to copy metadata, in addition to collecting
  data files. (`#113
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/113>`_)


2021.1 (2021-03-07)
-------------------


New hooks
~~~~~~~~~

* Add a hook for ``googleapiclient.model`` that collects the required
  metadata from the ``google-api-python-client`` package. (`#82
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/82>`_)
* Add hook for ``pyqtgraph``. (`#88
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/88>`_)
* Add hook for ``rpy2``. (`#87
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/87>`_)
* Added a hook for 'pdfminer.six' library (`#83
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/83>`_)
* Added a hook for the 'pygraphviz' library (`#86
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/86>`_)


Updated hooks
~~~~~~~~~~~~~

* Add missing ``dataclasses`` hidden import to ``pydantic`` hook.
  Add missing ``distutils.version`` hidden import to ``pydantic`` hook for
  versions of ``pydantic`` prior to ``1.4``. (`#81
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/81>`_)
* Update ``pydantic`` hook for compatibility with v.1.8.0 and later. (`#90
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/90>`_)


2020.11 (2020-12-21)
--------------------


New hooks
~~~~~~~~~

* Add a hook for ``gcloud`` which requires its distribution metadata. (`#68
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/68>`_)
* Add a hook for prettytable which requires its distribution metadata. (`#77
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/77>`_)
* Add hook for ``pydantic`` to improve support for its extension-compiled
  distribution (default on PyPi). (`#78
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/78>`_)
* Add hook for ``torchvision.ops`` to ensure that the required extension module
  (``torchvision._C``) is collected. (`#80
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/80>`_)
* Add hook for afmformats. (`#69
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/69>`_)
* Add hook for ijson which has dynamically loaded backends. (`#64
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/64>`_)
* Add hook for lxml which has hidden imports. (`#66
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/66>`_)
* Collect metadata and data files for ``countryinfo`` to support version 0.1.2.
  (`#76 <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/76>`_)


Updated hooks
~~~~~~~~~~~~~

* (Windows) Fix the ``win32com`` pre-safe-import hook to avoid printing the
  ``ModuleNotFoundError`` when the module is not available. (`#67
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/67>`_)
* Add default enabled sentry integrations dynamically to hidden imports. (`#71
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/71>`_)
* Update ``pyproj`` hook to improve compatibility across different versions of
  ``pyproj`` (from 2.1.3 to 3.0.0). (`#70
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/70>`_)


2020.10 (2020-10-29)
--------------------


New hooks
~~~~~~~~~

* (Windows) Add a hook for ``win32ctypes.core``. (`#58
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/58>`_)


Updated hooks
~~~~~~~~~~~~~

* (Windows) Avoid collecting ``tensorflow`` import libraries. (`#55
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/55>`_)
* Avoid collecting non-functional ``zmq.backend.cffi`` backend in the ``zmq``
  hook, and thus also prevent an attempt at compilation of its C extension
  during module collection. (`#59
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/59>`_)
* Change hook for ``tinycss2``, no longer needed after version 1.0.0. (`#54
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/54>`_)
* Compatibility fix for ``markdown`` 3.3. (`#56
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/56>`_)
* Update hooks for ``scikit-learn``. Supported versions are 0.21.x, 0.22.x, and
  0.23.x. (`#53
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/53>`_)


2020.9 (2020-10-02)
-------------------


New hooks
~~~~~~~~~

* Add a hook for `flask_restx <https://flask-restx.readthedocs.io>`_ which
  contains template data files. (`#48
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/48>`_)
* Add hooks for ``skimage.feature`` and ``skimage.graph`` to fix issues with
  missing imports. (`#52
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/52>`_)


Updated hooks
~~~~~~~~~~~~~

* Fix shared library duplication in ``tensorflow`` v.2.3. Avoid packaging
  unnecessary data files (e.g., development headers) on all ``tensorflow``
  versions. (`#50
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/50>`_)
* Fix the ``tensorflow`` hook to be compatible across ``tensorflow`` versions
  from <1.15.0 up to 2.3.0 (current latest). (`#46
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/46>`_)


2020.8 (2020-09-12)
-------------------


New hooks
~~~~~~~~~

* Add a hook for ``iminuit`` which has hidden imports. (`#26
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/26>`_)
* Add a hook for ``publicsuffix2`` which has some data files. (`#40
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/40>`_)
* Add a hook for ``pyav(av)`` which has hidden imports. (`#29
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/29>`_)
* Add a hook for ``pydivert`` which has some data files. (`#41
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/41>`_)
* Add a hook for ``pyproj`` which has some data files. (`#33
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/33>`_)
* Add a hook for ``spnego`` which has hidden imports. (`#37
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/37>`_)


Updated hooks
~~~~~~~~~~~~~

* Add a missing hidden import for ``passlib``. (`#39
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/39>`_)


2020.7 (2020-08-09)
-------------------


New hooks
~~~~~~~~~

* Add a hook for ``gmplot``, which has some data files. (`#21
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/21>`_)
* Add a hook for ``tinycss2``, which is missing data files. (`#16
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/16>`_)
* Add a hook for ``workflow``, which is missing version information contained
  in metadata. (`#17
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/17>`_)
* Add hook for ``AnyIO`` which dynamically imports its backend modules. (`#22
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/22>`_)
* Add hook for ``APScheduler`` which requires entry points and dynamic imports.
  (`#23 <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/23>`_)
* Add hook for ``trimesh`` which requires importing resource files. (`#25
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/25>`_)


Updated hooks
~~~~~~~~~~~~~

* Rewrite the hooks for PyPubSub and ``wx.lib.pubsub`` so they work properly.


2020.6 (2020-07-21)
-------------------


New hooks
~~~~~~~~~

* Add a hook for ``html-testRunner``, which has a hidden import. (`#8
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/8>`_)
* Add a hook for ``parsedatetime``, which has hidden imports. (`#11
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/11>`_)
* Add hook for ``dask``, which includes .yaml data files. (`#12
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/12>`_)


Updated hooks
~~~~~~~~~~~~~

* (Windows) cv2: bundle the `opencv_videoio_ffmpeg*.dll`, if available. (`#13
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/13>`_)


2020.5 (2020-06-28)
-------------------


No significant changes.


2020.4 (2020-06-28)
-------------------


New hooks
~~~~~~~~~

* Adding a hook for sentry which has hidden imports for its integrations (`#7
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/7>`_)


2020.3 (2020-06-21)
-------------------


New hooks
~~~~~~~~~

* Add a hook for ``eel``, which needs to pull in ``eel.js`` and an extra
  library. (`#6
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/6>`_)
* Add a hook for ``sklearn``, which needs a dynamic library including. (`#5
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/5>`_)
* Add hook for ``jinxed``, which has hidden backends.
