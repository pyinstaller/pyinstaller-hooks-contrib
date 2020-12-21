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
