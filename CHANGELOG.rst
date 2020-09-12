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
