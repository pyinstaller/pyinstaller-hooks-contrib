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
