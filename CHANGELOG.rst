2025.11 (2025-12-23)
--------------------

New hooks
~~~~~~~~~

* Add a hook for ``tkinterweb-tkhtml-extras``. (`#972
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/972>`_)
* Add hook for ``pymeshlab``. (`#975
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/975>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``skimage`` hooks for compatibility with ``scikit-image`` 0.26.0.
  (`#976
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/976>`_)


Incompatible Changes
~~~~~~~~~~~~~~~~~~~~

* The hooks for following modules/packages have been ported to
  ``PyInstaller.isolated``
  framework and therefore require PyInstaller >= 5.0:
  - ``win32com``
  - ``wx.lib.activex``
  - ``enchant``
  - ``sentry_sdk``
  - ``ffpyplayer``
  If you are still using PyInstaller 4.x and any of these packages, make sure
  to
  pin an older version of ``pyinstaller-hooks-contrib``. (`#970
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/970>`_)


2025.10 (2025-11-22)
--------------------

New hooks
~~~~~~~~~

* Add hook for ``dateparser`` to collect the data file that was introduced
  in ``dateparser`` v.1.2.2. (`#958
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/958>`_)
* Add hook for ``duckdb`` to ensure that ``inspect`` module is collected
  (might end up missing with python < 3.10 otherwise), and that the
  package's metadata is collected for ``duckdb`` >= 1.4.0. (`#952
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/952>`_)
* Add hook for ``nicegui`` to collect the data files of the package. (`#962
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/962>`_)
* Add hook for ``psycopg_binary`` (binary installation Psycopg 3) to ensure
  that ``psycopg_binary._uuid`` module is collected, in order to prevent
  missing-module error when working with data of UUID data type. (`#956
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/956>`_)
* Add hook for ``pyecharts`` to collect the data files of the package. (`#963
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/963>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``langchain`` hooks for ``langchain`` v.1.0.x. (`#960
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/960>`_)


2025.9 (2025-09-24)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``cumm`` to ensure that header files from ``cumm/include``
  directory are collected. (`#941
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/941>`_)
* Add hook for ``globus_sdk`` package. (`#940
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/940>`_)
* Add hook for ``pointcept`` to collect its source .py files for
  TorchScript/JIT. (`#941
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/941>`_)


Updated hooks
~~~~~~~~~~~~~

* Harden ``blib2to3`` and ``torch`` hooks against missing ``RECORD`` in
  the corresponding distributions' metadata, which would lead to a
  ``'NoneType' object is not iterable`` error when the hook tries to iterate
  over distribution's file list. (`#942
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/942>`_)
* Update ``numba`` hook for changes made in ``numba`` v0.62.0 (i.e., removal
  of the new type system that was previously introduced in v0.61 series).
  (`#949
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/949>`_)
* Update ``torch`` hook to check whether ``torch`` is installed via
  Anaconda ``pytorch`` package, and collect DLLs from Anaconda ``mkl``
  package and its dependencies, if necessary. (`#941
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/941>`_)


2025.8 (2025-07-27)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``uuid6``, which, starting with version 2025.0.1, requires
  its metadata to be collected. (`#929
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/929>`_)


Updated hooks
~~~~~~~~~~~~~

* `shapely` hook: extend the search for `geos_c` DLL to also look for an
  alternative name with `lib` prefix (i.e., `libgeos_c`), which is used
  in `MSYS2` environment. (`#927
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/927>`_)
* Adjust the value of automatically-raised recursion limit (which :issue:`925`
  set at 5000); for Windows builds of python 3.8 - 3.10 and python
  3.9 available under Cygwin, the value needs to be lowered to 1900, as
  higher values lead to python interpreter crash in scenarios when recursion
  level actually approaches the limit (for example, the recursion limit
  test in the main PyInstaller repository). (`#928
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/928>`_)
* Update ``gribapi`` hook for compatibility with ``eccodes`` 2.43.0; add
  hooks for ``eccodeslib``, ``eckitlib``, and ``fckitlib``, which now
  provide the bundled shared libraries on non-Windows systems. (`#930
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/930>`_)
* Update the run-time hook for ``findlibs`` for improved compatibility
  with ``findlibs`` > 1.0.0; avoid providing a default value for
  ``pkg_name`` argument in our ``findlibs.find()`` override, and instead
  forward the original value (i.e., ``None``) to the original ``find()``
  implementation. (`#930
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/930>`_)


2025.7 (2025-07-22)
-------------------

Updated hooks
~~~~~~~~~~~~~

* Automatically raise the recursion limit to at least 5000 when the
  ``_pyinstaller_hooks_contrib`` module is loaded, rather than raising
  the recursion limit on per-hook basis. (`#925
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/925>`_)
* Update ``sklearn`` hooks for compatibility with ``scikit-learn`` 1.7.1.
  (`#925
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/925>`_)


2025.6 (2025-07-14)
-------------------

New hooks
~~~~~~~~~

* Add a hook for ``pynng``, which has a hidden import. (`#922
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/922>`_)
* Add hook for ``torchao`` to collect its source .py files for TorchScript/JIT.
  (`#917
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/917>`_)
* Add hooks for new modules that were introduced in ``vtk`` 9.5.0:
  ``vtkmodules.vtkIOAvmesh``, ``vtkmodules.vtkIOLANLX3D``,
  ``vtkmodules.vtkRenderingGridAxes``, and
  ``vtkmodules.vtkTestingSerialization``. (`#919
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/919>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``plotly`` hook for compatibility with ``plotly`` 6.2.0. (`#919
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/919>`_)
* Update ``pylsl`` hook for compatibility with ``pylsl`` >= 1.17.0. (`#924
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/924>`_)
* Update ``toga`` hook for compatibility with ``toga`` 0.5.2: ensure that
  ``toga/__init__.pyi``  file is collected. (`#923
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/923>`_)


2025.5 (2025-06-08)
-------------------

New hooks
~~~~~~~~~

* Extend hooks for ``slearn`` to fix compatibility with ``scikit-learn``
  v1.7.0; add hooks for ``sklearn.externals.array_api_compat.cupy``,
  ``sklearn.externals.array_api_compat.dask.array``,
  ``sklearn.externals.array_api_compat.numpy``, and
  ``sklearn.externals.array_api_compat.torch`` that specify hidden imports
  for corresponding ``.linalg`` and ``.fft`` sub-modules, which are
  imported with using ``__import__()`` function and programmatically-generated
  names. (`#915
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/915>`_)


Updated hooks
~~~~~~~~~~~~~

* ``usb`` hook: fix shared library collection on Windows. (`#906
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/906>`_)
* Have the ``_load_library`` override installed by the ``usb`` run-time
  hook honor the passed ``find_library`` argument. (`#913
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/913>`_)


2025.4 (2025-05-03)
-------------------

Updated hooks
~~~~~~~~~~~~~

* Fix error in ``narwhals`` hook when ``typing-extensions`` is not available
  in the build environment (neither stand-alone version is installed
  nor it is provided as part of ``setuptools``). (`#908
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/908>`_)


2025.3 (2025-04-16)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``apkutils`` which requries to collect its XML file. (`#894
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/894>`_)
* Add hook for ``emoji``. (`#891
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/891>`_)
* Add hook for ``frictionless`` to collect package's data files, and
  programmatically imported modules from ``frictionless.plugins``. (`#897
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/897>`_)
* Add hook for ``narwhals`` to collect metadata for ``typing-extensions``,
  which is required starting with ``narwhals`` v1.35.0. (`#901
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/901>`_)
* Add hooks for ``black`` and ``blikb2to3`` packages from the ``black``
  dist to collect hidden imports and data files. (`#897
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/897>`_)
* Add hooks for ``tkinterweb``, to collect data files, and
  ``tkinterweb-tkhtml``, to collect extra data files and binaries. (`#899
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/899>`_)
* Add hooks for ``urllib3`` and ``urllib3_future`` to handle indirect
  imports made by the ``urllib3-future`` implementation of the ``urllib3``
  package and its own ``urllib3_future`` package. (`#893
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/893>`_)
* Add hooks for all submodules of ``vtkmodules`` package, which is
  installed by the ``vtk`` dist (currently targeting v9.4.2). (`#896
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/896>`_)


Updated hooks
~~~~~~~~~~~~~

* Update hook for ``pydantic`` to always collect submodules from the package,
  in order to properly handle redirections and programmatic imports found
  in contemporary versions of ``pydantic``. (`#897
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/897>`_)


2025.2 (2025-03-23)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``distributed`` package (i.e., ``dask.distributed``) to
  collect its data files and modules from ``distributed.http``. (`#877
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/877>`_)
* Add hook for ``niquests``. (`#888
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/888>`_)
* Add hook for ``python-dateutil`` to collect data files from the package.
  (`#881
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/881>`_)
* Add hook for ``tkinterdnd2`` (>= 0.4.0) that collects shared library and
  .tcl files from platform-specific sub-directory under ``tkinterdnd2/tkdnd``.
  (`#868
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/868>`_)


Updated hooks
~~~~~~~~~~~~~

* Fix ``pyqtgraph.multiprocess`` in combination with PyInstaller >= v6.10.0.
  (`#886
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/886>`_)
* Fix path matching for MKL DLLs in ``torch`` hook to work with either
  POSIX-style or Windows-style separators, as either can appear in the
  metadata's RECORD entries. (`#879
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/879>`_)
* Update ``h5py`` hook to handle Debian's ``python3-h5py`` distribution of
  ``h5py``. (`#873
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/873>`_)
* Update ``pyproj`` hook to handle non pip/PyPI distributions' devendoring its
  data directory. (`#873
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/873>`_)
* Update ``rtree`` hook for compatibility with ``rtree`` 1.4.0 (renamed
  shared library directory in Linux PyPI wheels). (`#875
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/875>`_)
* Update ``toga`` hook for compatibility with ``toga`` v0.5.0. Due to
  refactor of the main module that introduced lazy import of package's
  submodules, we now need to explicitly collect the said submodules using
  the ``collect_submodules`` helper. (`#878
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/878>`_)
* Update hook for ``travertino`` to explicitly collect the package's metadata
  in order to fix compatibility with ``travertino`` v0.5.0. (`#878
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/878>`_)
* Update the ``findlibs`` run-time hook to gracefully handle ``TypeError``
  when using ``findlibs`` v0.1.0 with python < 3.10. This prevents the
  frozen application from crashing on the run-time hook when the main
  code might never end up using/importing ``findlibs`` at all (for example,
  ``gribapi`` module from ``eccodes`` when binary wheel with bundled
  shared libraries is used). (`#865
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/865>`_)


2025.1 (2025-01-31)
-------------------

New hooks
~~~~~~~~~

* Add hooks for ``pypdfium2`` and ``pypdfium2_raw``. (`#860
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/860>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``numba`` hook for compatibility with ``numba`` v0.61.0. (`#857
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/857>`_)
* Update ``numcodecs`` hook for compatibility with ``numcodecs`` v0.15.0.
  (`#858
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/858>`_)


2025.0 (2025-01-16)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``fsspec`` to collect the package's submodules
  and ensure the protocol plugins are working. (`#856
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/856>`_)
* Add hook for ``intake`` to collect its plugins (registered via the
  ``intake.drivers`` entry-point). (`#853
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/853>`_)
* Add hook for ``ruamel.yaml`` to collect its plugins, and ensure that
  plugins' ``__plug_in__`` modules are collected as source .py files
  (which is necessary for their discovery). (`#844
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/844>`_)
* Add hook for ``sam2`` (Segment Anything Model 2). (`#847
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/847>`_)
* Add hook for ``zarr`` to collect the package's metadata. (`#855
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/855>`_)


Updated hooks
~~~~~~~~~~~~~

* Revise the search for OpenSSL shared library and ``ossl-modules`` directory
  in the ``cryptography`` hook, in order to mitigate issues with unrelated
  copies of OpenSSL ending up being pulled into the build. Most notably,
  the hook should not be searching for OpenSSL shared library when
  ``cryptography`` PyPI wheel is installed, because those ship with
  extensions that are statically linked against OpenSSL. (`#846
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/846>`_)
* Rewrite ``pygraphviz`` hook to fix discovery and collection of ``graphviz``
  files under various Linux distributions, in Anaconda environments
  (Windows, Linux, and macOS), and msys2 environments (Windows). (`#849
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/849>`_)
* Update ``dask`` hook to collect template files from
  ``dask/widgets/templates``
  directory; these file become mandatory when using ``dask.array`` and
  ``jinja2`` is available. (`#852
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/852>`_)
* Update ``triton`` hook for compatibility with ``triton`` >= 3.0.0; the
  hook should now collect backend-specific modules and data files from
  ``triton.backends``. (`#848
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/848>`_)


2024.11 (2024-12-23)
--------------------

New hooks
~~~~~~~~~

* Add hook for ``selectolax`` to collect its data files. (`#841
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/841>`_)


Updated hooks
~~~~~~~~~~~~~

* (Linux) Update ``torch`` hook to suppress creation of symbolic links to
  the top-level application directory for the shared libraries discovered
  during binary dependency analysis in ``torch/lib`` directory. This fixes
  issues with ``libtorch_cuda_linalg.so`` not being found in spite of it
  being collected, as observed with certain ``torch`` builds provided by
  https://download.pytorch.org/whl/torch (e.g., ``1.13.1+cu117``,
  ``2.0.1+cu117``, and ``2.1.2+cu118``). (`#834
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/834>`_)
* Update ``sklearn.tree`` hook for compatibility with ``scikit-learn`` v1.6.0
  (add ``sklearn.tree._partitioner`` to hidden imports). (`#838
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/838>`_)


2024.10 (2024-11-10)
--------------------

New hooks
~~~~~~~~~

* Add hook for ``h3`` to collect its metadata (required with ``h3`` v4.0.0
  and later). (`#825
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/825>`_)
* Add hook for ``numbers_parser`` to ensure that package's data file is
  collected. (`#823
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/823>`_)
* Add hook for ``sv_ttk`` to ensure that its resources (.tcl files and
  images) are collected. (`#826
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/826>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``falcon`` hook for compatibility with ``falcon`` v4.0.0. (`#820
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/820>`_)
* Update ``tensorflow`` hook to automatically raise recursion limit to
  5000 (if not already set to a higher value) in order to avoid recursion
  limit errors in certain import chains (dependent on build environment
  and other packages installed in it). (`#825
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/825>`_)


2024.9 (2024-10-15)
-------------------

New hooks
~~~~~~~~~

* Add a hook for comtypes to ensure compatibility with comtypes >= 1.4.5.
  (`#807
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/807>`_)
* Add analysis hook for ``slixmpp`` library (`#784
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/784>`_)
* Add hook for ``capstone`` package. (`#787
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/787>`_)
* Add hook for ``grapheme`` to collect its data files. (`#793
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/793>`_)
* Add hook for ``onnxruntime`` to ensure that provider plugins are
  collected. (`#817
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/817>`_)
* Add hook for ``saml2`` package which has XSD files and hidden imports. (`#798
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/798>`_)
* Add hook for ``setuptools_scm`` that collects metadata of ``setuptools``
  dist in order to avoid run-time warning about unknown/incompatible
  ``setuptools`` version. (`#805
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/805>`_)
* Add hook for ``ultralytics`` package. (`#786
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/786>`_)
* Add hook for ``xmlschema`` package which has XSD files. (`#797
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/797>`_)
* Add hook for ``yapf_third_party`` (part of ``yapf``) to collect its
  data files. (`#792
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/792>`_)
* Add hooks for ``toga`` widget toolkit and its backends. (`#804
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/804>`_)
* Add run-time hook for ``findlibs`` that overrides the ``findlibs.find``
  function with custom implementation in order to ensure that the top-level
  application directory is searched first. This prevents a system-wide
  copy of the library being found and loaded instead of the bundled copy
  when the system-wide copy happens to be available in one of fixed
  locations that is scanned by the original implementation of ``findlibs.find``
  (for example, Homebrew directory on macOS). (`#799
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/799>`_)


Updated hooks
~~~~~~~~~~~~~

* (Linux) Update ``tensorflow`` hook to suppress creation of symbolic links
  to the top-level application directory for the following shared libraries
  discovered during binary dependency analysis: ``libtensorflow_cc.so.2``,
  ``libtensorflow_framework.so.2``, and ``_pywrap_tensorflow_internal.so``.
  This fixes run-time discovery of CUDA shared libraries from ``nvidia.cu*``
  packages. This fix requires PyInstaller >= 6.11 to work, and is no-op
  in earlier PyInstaller versions. (`#786
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/786>`_)
* (Linux) Update hooks for ``nvidia.cu*`` packages to suppress creation of
  symbolic links to the top-level application directory for all shared
  libraries collected from the packages. This fixes run-time discovery
  of other shared libraries from those packages, which are dynamically
  loaded at run-time (as opposed to being linked against). Specifically,
  this fixes the ``Unable to load any of
  {libcudnn_engines_precompiled.so.9.1.0,
  libcudnn_engines_precompiled.so.9.1, libcudnn_engines_precompiled.so.9,
  libcudnn_engines_precompiled.so}`` and subsequent
  ``RuntimeError: CUDNN_BACKEND_TENSOR_DESCRIPTOR cudnnFinalize failed
  cudnn_status: CUDNN_STATUS_NOT_INITIALIZED`` when trying to use
  ``ultralytics`` package. This fix requires PyInstaller >= 6.11 to work,
  and is no-op in earlier PyInstaller versions. (`#786
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/786>`_)
* Update ``av`` hook for compatibility with ``av`` v13.0.0. (`#794
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/794>`_)
* Update ``av`` hook for compatibility with ``av`` v13.1.0. (`#814
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/814>`_)
* Update ``gribapi`` hook for compatibility with ``eccodes`` v2.37.0,
  to account for possibility of bundles ``eccodes`` shared library, which
  is provided by newly-introduced binary wheels for Linux and macOS 13+. (`#799
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/799>`_)
* Update ``pydicom`` hook for compatibility with ``pydicom`` v.3.0.0. (`#796
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/796>`_)
* Update ``xarray`` hook to collect ``xarray.chunkmanagers`` entry-points.
  (`#800
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/800>`_)


2024.8 (2024-08-09)
-------------------

New hooks
~~~~~~~~~

* Add a hook for ``cmocean``, which has text data files. (`#769
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/769>`_)
* Add a hook for ``pydicom``, which has hidden imports. (`#776
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/776>`_)
* Add a hook for ``tzwhere``, which has data files. (`#772
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/772>`_)
* Add hook for ``monai`` to collect its source .py files for TorchScript/JIT.
  (`#778
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/778>`_)
* Add hooks for ``itk`` to work around the package's requirements about
  the ``itk/Configuration`` directory. (`#778
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/778>`_)
* Added hooks for the ``trame`` suite of libraries, which has data files and
  hidden imports. (`#775
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/775>`_)


Updated hooks
~~~~~~~~~~~~~

* Rework the OpenSSL version check in ``cryptography`` hook to fix
  compatibility with ``cryptography`` 43.0.0. (`#768
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/768>`_)
* Update ``hydra`` hook to include work-around for ``hydra``'s plugin
  manager, which under python < 3.10 (still) uses deprecated PEP-302
  that was removed from PyInstaller's ``PyiFrozenImporter`` in
  PyInstaller 5.8. When building using python < 3.10 and PyInstaller >= 5.8,
  the modules collected from ``hydra._internal.core_plugins`` and
  ``hydra_plugins`` packages are now collected as source .py files only;
  this way, they are handled by built-in python's finder/importer instead
  of PyInstaller's ``PyiFrozenImporter``. (`#760
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/760>`_)
* Update ``imageio_ffmpeg`` hook for compatibility with ``imageio-ffmpeg``
  0.5.0 and later. (`#766
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/766>`_)
* Update ``pyexcel_ods`` hook to add missing hidden import and add tests.
  (`#779
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/779>`_)


Project & Process
~~~~~~~~~~~~~~~~~

* Released sdists and tagged GitHub source archives contain the changelog
  entries
  for their current release. (`#761
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/761>`_)


2024.7 (2024-06-08)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``dbus_fast`` in order to collect submodules that are imported
  from cythonized extensions. (`#600
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/600>`_)
* Add hook for ``gribapi`` package from ``eccodes`` dist, in order to
  collect bundled headers and ensure that the eccodes shared library is
  collected from the build environment. (`#744
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/744>`_)
* Add hook for ``patoolib`` to collect dynamically-imported modules from
  the ``patoolib.programs`` sub-package. (`#748
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/748>`_)


Updated hooks
~~~~~~~~~~~~~

* Extend the ``xarray`` hook to collect additional backend plugins that are
  registered via the ``xarray.backends`` entry-point (e.g., ``cfgrib``). (`#744
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/744>`_)


2024.6 (2024-05-10)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``schwifty``. Requires ``schwifty >= 2024.5.1`` due to
  issues with data search path in earlier versions. (`#742
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/742>`_)


2024.5 (2024-04-23)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``backports`` package, to accommodate the ``pkgutil``-style
  ``backports`` namespace package provided by ``backports.functools-lru-cache``
  and the latest release of ``backports.tarfile``. (`#735
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/735>`_)
* Add hook for ``opentelemetry`` that collects all entry-points with
  ``opentelemetry_`` prefix. (`#725
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/725>`_)
* Add hook for ``skimage.metrics`` to account for lazy loading of the
  ``skimage.metrics`` that was introduced in ``scikit-image`` 0.23.0. (`#723
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/723>`_)
* Add hook for ``xarray``, which ensures that metadata for ``numpy``
  (required by ``xarray``) is collected. (`#728
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/728>`_)


Updated hooks
~~~~~~~~~~~~~

* (Windows) Update ``pyproj`` hook to explicitly collect DLLs and
  load-order file (if present) from ``pyproj.libs`` directory. This
  fixes ``DLL load failed while importing _network`` error when using
  Anaconda python 3.8 or 3.9, where ``delvewheel`` (used by ``pyproj``)
  needs to load DLLs via load-order file due to defunct
  ``os.add_dll_directory`` function. (`#726
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/726>`_)
* Extend ``cryptography`` hook to collect OpenSSL modules (the
  ``ossl-modules`` directory) when available. Add a run-time hook that
  overrides OpenSSL module search path by setting the ``OPENSSL_MODULES``
  environment variable to the bundled ``ossl-modules`` directory. This
  fixes ``RuntimeError: OpenSSL 3.0's legacy provider failed to load.``
  error when using ``cryptography`` with OpenSSL >= 3.0 builds that have
  modules enabled (e.g., most Linux distributions, msys/MinGW on Windows,
  and Homebrew on macOS). (`#724
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/724>`_)
* Suppress errors in ``gcloud`` hook that occur when the hook is triggered
  by the ``gcloud`` namespace package from ``gcloud-aio-*`` and
  ``gcloud-rest-*``
  dists instead of the ``gcloud`` package from the ``gcloud`` dist. (`#731
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/731>`_)
* Update hook for ``tables`` (PyTables) to collect bundled blosc2
  shared library, if available. On Windows, explicitly collect DLLs and
  load-order file (if present) from ``tables.libs`` directory. (`#732
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/732>`_)


2024.4 (2024-04-13)
-------------------

New hooks
~~~~~~~~~

* Add a hook for ``python-pptx``, including required template files. (`#719
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/719>`_)
* Add hook for ``cloudpickle`` to ensure that ``cloudpickle.cloudpickle_fast``
  is collected when using ``cloudpickle`` v3.0.0 or later. (`#716
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/716>`_)
* Add hook for ``hexbytes`` that collects package's metadata (required
  starting with ``hexbytes`` v.1.1.0). (`#714
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/714>`_)


Updated hooks
~~~~~~~~~~~~~

* (Windows) Update ``netCDF4`` hook to explicitly collect DLLs and
  load-order file (if present) from ``netCDF4.libs`` directory. This
  fixes ``DLL load failed while importing _netCDF4`` error when using
  Anaconda python 3.8 or 3.9, where ``delvewheel`` (used by ``netCDF4``)
  needs to load DLLs via load-order file due to defunct
  ``os.add_dll_directory`` function. (`#722
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/722>`_)
* Update ``adbutils`` hooks for compatibility with ``adbutils`` v2.2.2 and
  later. (`#717
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/717>`_)
* Update ``numba`` hook to ensure that ``numba.cloudpickle.cloudpickle_fast``
  is collected when using ``numba`` v0.59.0 or later. (`#716
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/716>`_)
* Update ``tensorflow`` hooks for compatibility with ``tensorflow`` v2.16.0.
  (`#714
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/714>`_)


2024.3 (2024-03-09)
-------------------

Updated hooks
~~~~~~~~~~~~~

* Update ``torch`` hook to add support for MKL-enabled ``torch`` builds
  on Windows (e.g., the nightly ``2.3.0.dev20240308+cpu`` build). The hook
  now attempts to discover and collect DLLs from MKL and its dependencies
  (``mkl``, ``tbb``, ``intel-openmp``). (`#712
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/712>`_)


2024.2 (2024-02-29)
-------------------

New hooks
~~~~~~~~~

* Add a hook for ``iso639-lang``, to collect data files (`#707
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/707>`_)
* Add hook for ``falcon``, which has hidden imports. (`#703
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/703>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``pyqtgraph`` hook to use the helper for automatic Qt bindings
  selection and exclusion from PyInstaller >= 6.5 (no-op with earlier
  versions). This should help preventing multiple Qt bindings from
  being collected into frozen application. (`#710
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/710>`_)
* Update the exclude list for GUI frameworks in the ``IPython`` hook with
  additional contemporary Qt bindings (``PySide2``, ``PySide6``, and
  ``PyQt6``). (`#708
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/708>`_)


2024.1 (2024-02-10)
-------------------

Updated hooks
~~~~~~~~~~~~~

* Fix hook for ``osgeo``, to include proj data files. (`#693
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/693>`_)
* Update the hook for ``sklearn.neighbors`` to account for removed hidden
  import ``neighbors._typedef`` (`#698
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/698>`_)


2024.0 (2024-01-18)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``cel-python``. (`#687
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/687>`_)
* Add hook for ``eth_keys`` that collects package metadata for
  ``eth-keys >= 0.5.0``. (`#688
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/688>`_)
* Add hook for ``fairscale`` to collect its source .py files for
  TorchScript/JIT. (`#692
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/692>`_)
* Add hook for ``pygwalker`` that collects data files from the package. (`#690
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/690>`_)
* Add hook for ``PyTaskbar`` (`#684
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/684>`_)


Updated hooks
~~~~~~~~~~~~~

* Collect package metadata for ``eth-hash`` (fixes ``PackageNotFoundError``).
  (`#688
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/688>`_)
* Update ``pypylon`` hook for compatibility with PyInstaller 6.0 and later.
  (`#691
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/691>`_)


2023.12 (2024-01-03)
--------------------

New hooks
~~~~~~~~~

* Add hook for ``detectron2`` to collect its source .py files for
  TorchScript/JIT. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for ``fastai`` to collect its source .py files for TorchScript/JIT.
  (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for ``fvcore.nn`` to collect its source .py files for
  TorchScript/JIT. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for ``langchain`` that collects data files from the package. (`#681
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/681>`_)
* Add hook for ``lightning`` (PyTorch Lightning) to ensure that its
  ``version.info`` data file is collected. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for ``linear_operator`` to collect its source .py files for
  TorchScript/JIT. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for ``seedir`` that collects the ``words.txt`` data file from
  the package. (`#681
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/681>`_)
* Add hook for ``timm`` (Hugging Face PyTorch Image Models) to collect its
  source .py files for TorchScript/JIT. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for ``torchaudio`` that collects dynamically-loaded extensions,
  as well as source .py files for TorchScript/JIT. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for ``torchtext`` that collects dynamically-loaded extensions,
  as well as source .py files for TorchScript/JIT. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for ``torchvision.io.image`` to ensure that dynamically-loaded
  extension, required by this module, is collected. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for ``VADER``. (`#679
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/679>`_)
* Add hook for Hugging Face ``datasets`` to collect its source .py files for
  TorchScript/JIT. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hook for Hugging Face ``transformers``. The hook attempts to
  automatically collect the metadata of all dependencies (as declared
  in `deps` dictionary in the `transformers.dependency_versions_table`
  module), in order to make dependencies available at build time visible
  to ``transformers`` at run time. The hook also collects source .py files
  as some of the package's functionality uses TorchScript/JIT. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hooks for ``bitsandbytes``, and its dependency ``triton``. Both
  packages have dynamically-loaded extension libraries that need to be
  collected, and both require collection of source .py files for
  (``triton``'s) JIT module. Some submodules of ``triton`` need to be
  collected only as source .py files (bypassing PYZ archive), because the
  code naively assumes that ``__file__`` attribute points to the source
  .py file. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Add hooks for ``nvidia.*`` packages, which provide a way of installing
  CUDA via PyPI wheels (e.g., ``nvidia-cuda-runtime-cu12``). (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)


Updated hooks
~~~~~~~~~~~~~

* (Linux) Extend ``tensorflow`` hook to automatically collect CUDA libraries
  distributed via ``nvidia-*`` packages (such as ``nvidia-cuda-runtime-cu12``)
  if they are specified among the requirements in the ``tensorflow``
  distribution's metadata. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* (Linux) Extend ``torch`` hook to automatically collect CUDA libraries
  distributed via ``nvidia-*`` packages (such as ``nvidia-cuda-runtime-cu12``)
  if they are specified among the requirements in the ``torch`` distribution's
  metadata. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* (Linux) Remove the ``tensorflow.python._pywrap_tensorflow_internal``
  hack in the ``tensorflow`` hook (i.e., adding it to excluded modules
  to avoid duplication) when using PyInstaller >= 6.0, where the
  duplication issue is alleviated thanks to the binary dependency analysis
  preserving the parent directory layout of discovered/collected shared
  libraries. This should fix the problem with ``tensorflow`` builds where
  the ``_pywrap_tensorflow_internal`` module is not used as a shared
  library, as seen in ``tensorflow`` builds for Raspberry Pi. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* (Linux) Update ``torch`` hook to explicitly collect versioned .so files
  in the new PyInstaller >= 6.0 codepath. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Extend ``tensorflow`` hook to collect plugins installed in the
  ``tensorflow-plugins`` directory/package. Have the run-time ``tensorflow``
  hook provide an override for ``site.getsitepackages()`` that allows us
  to work around a broken module file location check and trick ``tensorflow``
  into loading the collected plugins. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Update ``tensorflow`` hook to attempt to resolve the top-level distribution
  name and infer the package version from it, in order to improve version
  handling when the "top-level" ``tensorflow`` dist is not installed (for
  example, user installs only ``tensorflow-intel`` or ``tensorflow-macos``)
  or has a different name (e.g., ``tf-nightly``). (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Update ``tensorflow`` hook to collect source .py files for
  ``tensorflow.python.autograph`` in order to silence a run-time warning
  about AutoGraph not being available. (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Update ``torchvision`` hook to collect source .py files for TorchScript/JIT
  (requires PyInstaller >= 5.3 to take effect). (`#676
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/676>`_)
* Update hook for ``skimage.feature`` to collect the
  ``orb_descriptor_positions.txt`` data file, which is required by
  the ``skimage.feature.ORB`` class. (`#675
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/675>`_)


Removed hooks
~~~~~~~~~~~~~

* Remove hook for ``google.api``, which erroneously assumes that presence
  of the ``google.api`` namespace package implies availability of the
  ``google-api-core`` dist. (`#682
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/682>`_)


2023.11 (2023-12-20)
--------------------

New hooks
~~~~~~~~~

* Add a hook for ``freetype`` that collects the shared library that is
  bundled with ``freetype-py`` PyPI wheels. (`#674
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/674>`_)
* Add a hook for ``z3c.rml`` that collects the required subset of Bitstream
  Vera TTF fonts from the ``reportlab`` package. (`#674
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/674>`_)
* Add hook for ``eth_rlp``. (`#672
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/672>`_)
* Add hook for ``eth_typing`` which requires its package metadata. (`#656
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/656>`_)
* Add hook for ``eth_utils`` to collect its embedded JSON files. (`#656
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/656>`_)
* Add hook for ``rlp``. (`#672
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/672>`_)
* Add hook for ``sspilib`` that collects submodules of ``sspilib.raw``,
  most of which are cythonized extensions. (`#669
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/669>`_)


Updated hooks
~~~~~~~~~~~~~

* Modernize the hook for ``torch`` and reduce the amount of unnecessarily
  collected data files (header files and static libraries). Requires
  PyInstaller >= 6.0. (`#666
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/666>`_)
* Update ```pyarrow``` hook to collect all of the package's submodules. (`#662
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/662>`_)
* Update ``rtree`` hook for compatibility with ``Rtree >= 1.1.0``. (`#657
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/657>`_)
* Update ``sudachipy`` hook for ``sudachipy`` 0.6.8. (`#673
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/673>`_)


2023.10 (2023-10-13)
--------------------

New hooks
~~~~~~~~~

* Add hook for ``gmsh``. (`#650
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/650>`_)


Updated hooks
~~~~~~~~~~~~~

* If ``nltk_data`` can be found both in the frozen program and under the
  default location specified by ``NLTK``, the former should be preferred to the
  latter. (`#646
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/646>`_)
* Update ``skimage`` hooks for compatibility with ``scikit-image`` 0.22.0.
  (`#652
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/652>`_)
* Update ``tensorflow`` hook for compatibility with ``tensorflow`` 2.14.0.
  (`#647
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/647>`_)


2023.9 (2023-09-26)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``LaoNLP``. (`#644
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/644>`_)
* Add hook for ``PyThaiNLP``. (`#644
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/644>`_)


2023.8 (2023-08-29)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``eng_to_ipa``. (`#631
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/631>`_)
* Add hook for ``jieba``. (`#628
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/628>`_)
* Add hook for ``khmer-nltk``. (`#633
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/633>`_)
* Add hook for ``Lingua``. (`#626
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/626>`_)
* Add hook for ``opencc-python``. (`#627
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/627>`_)
* Add hook for ``pymorphy3``. (`#634
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/634>`_)
* Add hook for ``python-crfsuite``. (`#633
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/633>`_)
* Add hook for ``python-mecab-ko``. (`#632
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/632>`_)
* Add hook for ``simplemma``. (`#629
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/629>`_)
* Add hook for ``SudachiPy``. (`#635
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/635>`_)
* Add hook for ``wordcloud``. (`#630
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/630>`_)


Updated hooks
~~~~~~~~~~~~~

* Fix an issue with enchant 2 using a different directory (in MacPorts) (`#636
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/636>`_)


2023.7 (2023-08-18)
-------------------

New hooks
~~~~~~~~~

* Add a hook for ``psutil``, which has platform-dependent exclude list. (`#623
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/623>`_)
* Add hook for CtkMessagebox. (`#619
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/619>`_)
* Add hook for Litestar (`#625
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/625>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``graphql_query`` hook for compatibility with ``graphql-query``
  v1.2.0. (`#621
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/621>`_)


2023.6 (2023-07-20)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``ens`` package, required by ``web3`` v6.6.0 and later. (`#617
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/617>`_)
* Add hook for ``jsonschema_specifications`` to collect the data files
  that ``jsonschema`` v4.18.0 moved into a separate package. (`#614
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/614>`_)


2023.5 (2023-07-05)
-------------------

New hooks
~~~~~~~~~

* Add a hook for astropy-iers-data, which includes data. (`#608
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/608>`_)
* Add a hook for skyfield, which includes data. (`#607
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/607>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``pydantic`` hook for compatibility with ``pydantic`` v2.0.0. (`#611
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/611>`_)


2023.4 (2023-06-27)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``customtkinter`` (`#542
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/542>`_)
* Add hook for ``fastparquet``. (`#583
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/583>`_)
* Add hook for ``librosa``. (`#582
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/582>`_)
* Add hook for ``mistune`` that collects plugin modules, which are indirectly
  loaded starting with ``mistune`` v3.0.0. (`#605
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/605>`_)
* Add hook for ``sympy`` that automatically raises recursion limit
  to 5000 if ``sympy`` >= 1.12 is detected. (`#587
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/587>`_)
* Add hook for ``xyzservices``. (`#590
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/590>`_)
* Add hook for pylibmagic (`#581
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/581>`_)


Updated hooks
~~~~~~~~~~~~~

* Turn the hook for ``google.cloud`` into hook for ``google.cloud.core``
  by renaming it. This hook is trying to collect metadata for
  ``google-cloud-core``, whereas ``google.cloud`` is a namespace package
  that can be populated by other dists as well. Specifically,
  ``googleapis-common-protos`` puts some files there, and when
  ``google-cloud-core`` is not installed, the mis-named hook triggered a
  missing-metadata error. (`#605
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/605>`_)
* Update ``cairocffi`` hook for compatibility with ``cairocffi`` v1.6.0. (`#599
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/599>`_)
* Update ``netCDF4`` hook for compatibility with ``netCDF4`` v1.6.4. (`#599
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/599>`_)
* Update ``scikit-image`` hooks for compatibility with version 0.21.0. (`#594
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/594>`_)
* Update hook for ``bokeh`` to collect metadata for ``bokeh`` >= 3.0.0. (`#588
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/588>`_)
* Update hook for ``googleapiclient.model``, fixing missing discovery docs and
  improving test. (`#596
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/596>`_)


2023.3 (2023-05-11)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``graphql_query`` (`#579
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/579>`_)
* Add hook for ``pylsl`` (`#573
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/573>`_)


Updated hooks
~~~~~~~~~~~~~

* Remove no longer needed ``py`` hidden imports for ``pyshark >= 0.6``. (`#575
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/575>`_)
* Update ``pydantic`` hook hidden imports to include the optional dependency
  ``email_validator``. (`#576
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/576>`_)


2023.2 (2023-04-07)
-------------------

New hooks
~~~~~~~~~

* Add hooks for ``moviepy.audio.fx.all`` and ``moviepy.video.fx.all`` that
  collect all
  corresponding submodules, so that importing ``moviepy.editor`` from MoviePy
  works
  out-of-the-box in the frozen application. (`#559
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/559>`_)


Updated hooks
~~~~~~~~~~~~~

* Add automatic increase of recursion limit in the ``torch`` hook to ensure
  that
  recursion limit is at least 5000 if ``torch`` 2.0.0 or later is detected.
  (`#570
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/570>`_)
* Extend ``cv2`` hook with support for OpenCV built manually from source
  and for OpenCV installed using the official Windows installer. This
  support requires PyInstaller >= 5.3 to work properly. (`#557
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/557>`_)
* Update ``scikit-image`` hooks for compatibility with the 0.19.x series;
  account for lazy module loading in ``skimage.filters``. (`#565
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/565>`_)
* Update ``scikit-image`` hooks for compatibility with the 0.20.x series;
  account for switch to ``lazy_module`` in ``skimage.data`` and
  ``skimage.filters`` as well as in main package. Collect new data files
  that are now required by ``skimage.morphology``. (`#565
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/565>`_)
* Update the hook for ``tensorflow`` to be compatible with TensorFlow 2.12.
  (`#564
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/564>`_)


2023.1 (2023-03-16)
-------------------

Updated hooks
~~~~~~~~~~~~~

* Add work-around for ``ffpyplayer`` 4.3.5 and 4.4.0 trying to use
  ``site.USER_BASE``, which is ``None`` in  PyInstaller 5.5 and later
  due to removal of PyInstaller's fake ``site`` module. (`#545
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/545>`_)
* Add work-around for ``tensorflow`` < 2.3.0 trying to use
  ``site.USER_SITE``, which is ``None`` in  PyInstaller 5.5 and later
  due to removal of PyInstaller's fake ``site`` module. (`#546
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/546>`_)
* Prevent ``pyqtgraph`` hook from recursing into ``pyqgraph.examples``
  while scanning for submodules. (`#551
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/551>`_)
* Update ``sklearn`` hooks for compatibility with ``scikit-learn`` 1.2.0
  and 1.2.1. (`#547
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/547>`_)


Removed hooks
~~~~~~~~~~~~~

* Delete hook for ``yt_dlp`` which fixed the offending hidden import upstream
  in
  ``yt_dlp>=2022.07.18``. (`#556
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/556>`_)


2023.0 (2023-02-13)
-------------------

New hooks
~~~~~~~~~

* Add hook for ``minecraft-launcher-lib`` (`#536
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/536>`_)
* Add hook for ``nbt`` (`#537
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/537>`_)


Updated hooks
~~~~~~~~~~~~~

* Have ``fiona`` hook collect the package's data files (e.g., the
  projections database). (`#541
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/541>`_)
* Update ``fiona`` hook for compatibility with ``fiona`` 1.9.0. (`#541
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/541>`_)


2022.15 (2023-01-15)
--------------------

New hooks
~~~~~~~~~

* Add a hook for `easyocr <https://github.com/JaidedAI/EasyOCR>`_,
  which imports recognition backends via ``imporlib.import_module()``
  and has a number of datafiles for different languages.

  Users can set which languages to include datafiles for with a hook option.
  (`#530
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/530>`_)
* Add hook for ``charset-normalizer`` to fix ``ModuleNotFoundError: No module
  named 'charset_normalizer.md__mypyc'``. (`#534
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/534>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``shapely`` hook for compatibility with ``shapely >= 2.0.0``. (`#527
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/527>`_)


Project & Process
~~~~~~~~~~~~~~~~~

* Added `hooks-config.rst` document which documents hook options.
  It is referred to from README.md. (`#530
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/530>`_)


2022.14 (2022-12-04)
--------------------

New hooks
~~~~~~~~~

* Add hook for ``cf_units``. (`#521
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/521>`_)
* Add hook for ``cftime``. (`#521
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/521>`_)
* Add hook for ``compliance_checker``. (`#521
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/521>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``netCDF4`` hook for compatibility with v1.4.0 and later, where
  ``netcdftime`` has been renamed to ``cftime``. (`#521
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/521>`_)
* Update ``pydantic`` hook to include ``dotenv`` optional dependency. (`#524
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/524>`_)


2022.13 (2022-11-08)
--------------------

Updated hooks
~~~~~~~~~~~~~

* Update ``pyproj`` hook for compatibility with ``pyproj`` v3.4.0. (`#505
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/505>`_)


2022.12 (2022-11-05)
---------------------

New hooks
~~~~~~~~~

* Add hook for ``discid``. (`#506
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/506>`_)
* Add hook for ``exchangelib``. (`#508
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/508>`_)


2022.11 (2022-10-27)
---------------------

New hooks
~~~~~~~~~

* Add a hook for ``spiceypy``, which has binary files. (`#482
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/482>`_)
* Added a hook for ``ldfparser``. (`#483
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/483>`_)


Updated hooks
~~~~~~~~~~~~~

* Extend the ``sounddevice`` and ``soundfile`` hooks to collect
  system-installed shared libraries in cases when the libraries are
  not bundled with the package (i.e., linux PyPI wheels, Anaconda on
  all OSes). (`#487
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/487>`_)
* Fix a ``TypeError`` raised by the ``clr`` hook when ``pythonnet`` dist
  lacks the file list metadata. (`#486
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/486>`_)
* Have ``clr`` hook check for availability of the ``pythonnet`` before
  trying to query its metadata. Fixes an
  ``importlib.metadata.PackageNotFoundError``
  raised by the ``clr`` hook when the hook is triggered by a module or
  a package named ``clr`` other than the ``clr`` extension module from
  ``pythonnet``. (`#486
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/486>`_)
* Have the ``pyqtgraph`` hook collect the colormap files and their
  license files from the package. (`#501
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/501>`_)
* Implement preliminary support for handling subprocesses used by
  ``pyqtgraph.multiprocess``, for example in ``pyqtgraph``
  ``RemoteGraphicsView`` widget. The user is still required to ensure that
  stdlib's ``multiprocessing.freeze_support`` is called in the entry-point
  script before using ``pyqtgraph``. In addition, with ``onefile`` builds,
  the user must set the ``_MEIPASS2`` environment variable to the value
  of ``sys._MEIPASS`` before using ``pyqtgraph``. (`#501
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/501>`_)
* In ``clr`` hook for ``pythonnet`` collect the ``Python.Runtime.dll`` as
  a data file on non-Windows OSes to prevent errors during binary dependency
  analysis. (`#500
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/500>`_)


2022.10 (2022-08-31)
---------------------

New hooks
~~~~~~~~~

* Add geopandas data files for ``geopandas==0.10.2``. (`#400
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/400>`_)


2022.9 (2022-08-26)
--------------------

New hooks
~~~~~~~~~

* Add hook for Hydra config system (``hydra-core``). (`#424
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/424>`_)


Updated hooks
~~~~~~~~~~~~~

* Fixed ``pyqtgraph`` hook for PyInstaller 5.2. (`#465
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/465>`_)
* Update ``cv2`` hook to add support for versions that attempt to perform
  module
  substitution via ``sys.path`` manipulation (== 4.5.4.58, >= 4.6.0.66) when
  used
  in combination with PyInstaller that supports setting module collection mode
  in hooks (> 5.2). The  contents of the ``cv2`` package are now collected in
  source form to bypass PYZ archive and avoid compatibility issues with
  PyInstaller's  ``FrozenImporter`` (`#468
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/468>`_)
* Update ``pyshark`` hook to be compatible with versions ``>=0.5.2``. (`#477
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/477>`_)
* Update ``pywintypes`` and ``pythoncom`` hooks for compatibility with upcoming
  changes in PyInstaller's attempt at preserving DLL parent directory
  structure. (`#474
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/474>`_)
* Update ``tensorflow`` hook to opt-out of generating warnings for missing
  hidden imports, using hook variable introduced in PyInstaller >= 5.2. On
  earlier releases, this is no-op. (`#458
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/458>`_)


2022.8 (2022-07-08)
--------------------

New hooks
~~~~~~~~~

* Add hook for ``great_expectations``. (`#445
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/445>`_)
* Add hook for ``hdf5plugin``. (`#461
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/461>`_)
* Add hook for ``pandas_flavor`` to handle hidden imports in version 0.3.0
  of the package. (`#455
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/455>`_)
* Add hook for ``pyshark``. (`#449
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/449>`_)


Updated hooks
~~~~~~~~~~~~~

* (Linux) Ensure that OpenCV hook collects Qt plugins and font files that
  are bundled with linux versions of ``opencv-python`` PyPI wheels. (`#453
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/453>`_)
* Fix ``tensorflow`` not being collected at all when using ``tensorflow``
  2.8.0 or newer and importing only from the ``tensorflow.keras`` subpackage.
  (`#451
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/451>`_)
* Update ``clr`` (``pythonnet-2.5.x``) hook to ensure ``platform`` and
  ``warnings`` modules are collected via hidden imports. Starting with
  PyInstaller 5.1, these may not be collected as part of optional imports
  of other modules, so they need to be explicitly collected by this hook.
  (`#444
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/444>`_)
* Update ``mariadb`` hook for compatibility with 1.1.x series. (`#463
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/463>`_)
* Update ``scikit-learn`` hooks for compatibility with 1.0.x and 1.1.x series.
  (`#456
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/456>`_)


2022.7 (2022-06-07)
--------------------

New hooks
~~~~~~~~~

* Add a hook for ``limits``, which has a data files to collect. (`#442
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/442>`_)
* Add hook for ``yt_dlp`` to handle indirect import in ``yt-dlp v2022.05.18``.
  (`#438
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/438>`_)
* Add libraries for ``pypemicro==0.1.9`` (`#417
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/417>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``weasyprint`` hook with required binaries. (`#439
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/439>`_)


2022.6 (2022-05-26)
--------------------

Updated hooks
~~~~~~~~~~~~~

* Fix the filter function used with ``collect_submodules`` in the ``pylint``
  hook to properly exclude ``pylint.testutils``. (`#435
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/435>`_)
* Update ``sounddevice`` and ``soundfile`` hooks for PyInstaller 5.1
  compatibility. (`#432
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/432>`_)


2022.5 (2022-05-16)
--------------------

New hooks
~~~~~~~~~

* Add a hook for ``numcodecs``, which has a hidden import. (`#420
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/420>`_)
* Add hook for ``grpc`` roots.pem file which is used by grpc. (`#419
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/419>`_)
* Add hook for ``python-stdnum``. (`#412
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/412>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``mariadb`` hook to always include the ``decimal`` module as a
  hidden import, instead of implicitly relying on it being picked up due
  to import in some other, unrelated module. (`#426
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/426>`_)


2022.4 (2022-04-17)
--------------------

New hooks
~~~~~~~~~

* Add a hook for ``clr_loader`` (used by upcoming ``pythonnet`` 3.x) that
  collects the DLLs required by the default runtime (.NET Framework) loader
  on Windows. (`#406
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/406>`_)
* Add a hook for ``lark`` (used by ``commentjson`` and others) that loads the
  needed grammar files. (`#409
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/409>`_)
* Add fiona hidden imports for ``fiona==1.8.21``. (`#399
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/399>`_)


Updated hooks
~~~~~~~~~~~~~

* Update the ``av`` hook for compatibility with the new DLL directory layout
  used by
  Windows PyPI wheels from version 9.1.1 on. (`#408
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/408>`_)


2022.3 (2022-03-24)
--------------------

New hooks
~~~~~~~~~

* Add a hook for ``altair``, which has data files. (`#387
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/387>`_)
* Add a hook for ``cassandra``, which has Cython files. (`#391
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/391>`_)
* Add a hook for ``fabric``, which has data files. (`#390
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/390>`_)
* Add a hook for ``gitlab``, which has data files. (`#392
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/392>`_)


Updated hooks
~~~~~~~~~~~~~

* Update ``shapely`` hooks with compatibility fixes for version 1.8.1,
  where PyPI wheels have changed the shipped ``libgeos_c`` shared library
  location and/or name. (`#394
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/394>`_)
* Update `imageio` hooks to include the lazily-loaded `plugins` submodule.
  (`#396
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/396>`_)


2022.2 (2022-02-15)
-------------------

Updated hooks
~~~~~~~~~~~~~

* Fix hook for ``azurerm`` when ``pyinstaller >= 4.4"``. (`#283
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/283>`_)
* Fix hook for astropy when astropy >= 5.0. (`#381
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/381>`_)


2022.1 (2022-02-10)
-------------------

New hooks
~~~~~~~~~

* Add a hook for ``py`` which has dynamically loaded vendored submodules.
  This fixes compatibility with ``pytest >= 7.0.0``. (`#376
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/376>`_)
* Added a hook for ``orjson``, which has hidden imports. (`#378
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/378>`_)


2022.0 (2022-01-24)
-------------------

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
-------------------

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
-------------------

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
-------------------

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
* Fix harmless missing modules warnings when using ``scikit-learn >= 0.22``
  (`#276
  <https://github.com/pyinstaller/pyinstaller-hooks-contrib/issues/277>`_).


2021.2 (2021-06-26)
-------------------

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
