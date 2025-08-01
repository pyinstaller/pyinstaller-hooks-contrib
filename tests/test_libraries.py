# ------------------------------------------------------------------
# Copyright (c) 2024 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

import pathlib

import pytest

from PyInstaller import isolated
from PyInstaller.compat import is_darwin, is_linux, is_py39, is_win
from PyInstaller.utils.hooks import is_module_satisfies, can_import_module, get_module_attribute
from PyInstaller.utils.tests import importorskip, requires, xfail


@importorskip('fiona')
def test_fiona(pyi_builder):
    pyi_builder.test_source(
        '''
        import fiona
        '''
    )


@importorskip('fiona')
def test_fiona_transform(pyi_builder):
    # Test that fiona in frozen application has access to its projections database. If projection data is unavailable,
    # the transform becomes an identity transform.
    pyi_builder.test_source(
        """
        from fiona.transform import transform_geom
        from fiona.crs import from_epsg

        eiffel_tower = {
            'type': 'Point',
            'coordinates': (2.294694, 48.858093),
        }

        crs_source = from_epsg(4326)  # WGS84
        crs_target = from_epsg(25831)  # ETRS89 / UTM zone 31N

        transformed = transform_geom(crs_source, crs_target, eiffel_tower)
        print(f"Transformed point: {transformed}")

        # Expected coordinates: obtained by manually running this program unfrozen
        EXPECTED_COORDINATES = (448265.9146792292, 5411920.651338793)
        EPS = 1e-6

        delta = [abs(value - expected) for value, expected in zip(transformed["coordinates"], EXPECTED_COORDINATES)]
        print(f"Delta: {delta}")
        assert all([value < EPS for value in delta]), f"Delta {delta} exceeds threshold!"
        """
    )


@importorskip('jinxed')
def test_jinxed(pyi_builder):
    pyi_builder.test_source(
        '''
        import jinxed
        jinxed.setupterm('xterm')
        assert jinxed._terminal.TERM.terminfo is jinxed.terminfo.xterm
        '''
    )


@importorskip("geopandas")
def test_geopandas(pyi_builder):
    pyi_builder.test_source(
        '''
        import geopandas
        '''
    )


@importorskip('trimesh')
def test_trimesh(pyi_builder):
    pyi_builder.test_source(
        """
        import trimesh
        """
    )


@importorskip('apscheduler')
def test_apscheduler(pyi_builder):
    pyi_builder.test_source(
        """
        import asyncio
        import datetime
        import random
        import time

        from apscheduler.schedulers.asyncio import AsyncIOScheduler


        def tick():
            now = datetime.datetime.now(tz=datetime.timezone.utc)
            value = random.randint(0, 100)
            print(f"Tick! Current time is: {now}, random value: {value}")


        async def main():
            scheduler = AsyncIOScheduler()
            scheduler.add_job(tick, "interval", seconds=1)
            scheduler.start()

            # Run for five seconds
            start_time = time.time()
            while time.time() - start_time < 5.0:
                await asyncio.sleep(0.1)


        asyncio.run(main())
        """)


@importorskip('boto')
@xfail(reason='boto does not fully support Python 3')
def test_boto(pyi_builder):
    pyi_builder.test_script('pyi_lib_boto.py')


@xfail(reason='Issue #1844.')
@importorskip('boto3')
def test_boto3(pyi_builder):
    pyi_builder.test_source(
        """
        import boto3
        session = boto3.Session(region_name='us-west-2')

        # verify all clients
        for service in session.get_available_services():
            session.client(service)

        # verify all resources
        for resource in session.get_available_resources():
            session.resource(resource)
        """)


@xfail(reason='Issue #1844.')
@importorskip('botocore')
def test_botocore(pyi_builder):
    pyi_builder.test_source(
        """
        import botocore
        from botocore.session import Session
        session = Session()
        # verify all services
        for service in session.get_available_services():
            session.create_client(service, region_name='us-west-2')
        """)


@xfail(is_darwin, reason='Issue #1895.')
@importorskip('enchant')
def test_enchant(pyi_builder):
    pyi_builder.test_script('pyi_lib_enchant.py')


@importorskip('zmq')
def test_zmq(pyi_builder):
    pyi_builder.test_source(
        """
        import zmq
        print(zmq.__version__)
        print(zmq.zmq_version())
        # This is a problematic module and might cause some issues.
        import zmq.utils.strtypes
        """)


@importorskip('pylint')
def test_pylint(pyi_builder):
    pyi_builder.test_source(
        """
        # The following more obvious test doesn't work::
        #
        #   import pylint
        #   pylint.run_pylint()
        #
        # because pylint will exit with 32, since a valid command
        # line wasn't given. Instead, provide a valid command line below.

        from pylint.lint import Run
        Run(['-h'])
        """)


@importorskip('markdown')
def test_markdown(pyi_builder):
    # Markdown uses __import__ed extensions. Make sure these work by
    # trying to use the 'toc' extension, using both short and long format.
    pyi_builder.test_source(
        """
        import markdown
        print(markdown.markdown('testing',
            extensions=['toc']))
        print(markdown.markdown('testing',
            extensions=['markdown.extensions.toc']))
        """)


@importorskip('pylsl')
def test_pylsl(pyi_builder):
    pyi_builder.test_source(
        """
        import pathlib
        import pylsl

        print(f"version: {pylsl.__version__}")
        print(f"library version: {pylsl.library_version()}")
        print(f"library info: {pylsl.library_info()}")

        # Ensure that bundled shared library is used
        try:
            from pylsl.lib import lib as cdll  # pylsl >= 0.17.0
        except ImportError:
            from pylsl.pylsl import lib as cdll  # older versions

        print(f"cdll: {cdll}")
        pkg_path = pathlib.Path(pylsl.__file__).parent.resolve()
        cdll_path = pathlib.Path(cdll._name).resolve()
        print(f"pkg_path: {pkg_path}")
        print(f"cdll_path: {cdll_path}")
        assert pkg_path in cdll_path.parents, "Loaded shared library is not the bundled one!"
        """)


@importorskip('lxml')
def test_lxml_isoschematron(pyi_builder):
    pyi_builder.test_source(
        """
        # The import of this module triggers the loading of some
        # required XML files.
        from lxml import isoschematron
        """)


@importorskip('openpyxl')
def test_openpyxl(pyi_builder):
    pyi_builder.test_source(
        """
        # Test the hook to openpyxl
        from openpyxl import __version__
        """)


@importorskip('pyodbc')
def test_pyodbc(pyi_builder):
    pyi_builder.test_source(
        """
        # pyodbc is a binary Python module. On Windows when installed with easy_install
        # it is installed as zipped Python egg. This binary module is extracted
        # to PYTHON_EGG_CACHE directory. PyInstaller should find the binary there and
        # include it with frozen executable.
        import pyodbc
        """)


@importorskip('pyttsx')
def test_pyttsx(pyi_builder):
    pyi_builder.test_source(
        """
        # Basic code example from pyttsx tutorial.
        # http://packages.python.org/pyttsx/engine.html#examples
        import pyttsx
        engine = pyttsx.init()
        engine.say('Sally sells seashells by the seashore.')
        engine.say('The quick brown fox jumped over the lazy dog.')
        engine.runAndWait()
        """)


@importorskip('pyttsx3')
def test_pyttsx3(pyi_builder):
    pyi_builder.test_source("""
        import pyttsx3
        engine = pyttsx3.init()
    """)


@importorskip('pycparser')
def test_pycparser(pyi_builder):
    pyi_builder.test_script('pyi_lib_pycparser.py')


@importorskip('Crypto')
def test_pycrypto(pyi_builder):
    pyi_builder.test_source(
        """
        import binascii
        from Crypto.Cipher import AES
        BLOCK_SIZE = 16
        print('AES null encryption, block size', BLOCK_SIZE)
        # Just for testing functionality after all
        print('HEX', binascii.hexlify(
            AES.new(b"\\0" * BLOCK_SIZE, AES.MODE_ECB).encrypt(b"\\0" * BLOCK_SIZE)))
        from Crypto.PublicKey import ECC
        """)


@importorskip('Cryptodome')
def test_cryptodome(pyi_builder):
    pyi_builder.test_source(
        """
        from Cryptodome import Cipher
        from Cryptodome.PublicKey import ECC
        print('Cryptodome Cipher Module:', Cipher)
        """)


@importorskip('h5py')
def test_h5py(pyi_builder):
    pyi_builder.test_source("""
        import h5py
        """)


@importorskip('unidecode')
def test_unidecode(pyi_builder):
    pyi_builder.test_source("""
        from unidecode import unidecode

        # Unidecode should not skip non-ASCII chars if mappings for them exist.
        assert unidecode(u"kožušček") == "kozuscek"
        """)


@importorskip('pinyin')
def test_pinyin(pyi_builder):
    pyi_builder.test_source("""
        import pinyin
        """)


@importorskip('uvloop')
@pytest.mark.darwin
@pytest.mark.linux
def test_uvloop(pyi_builder):
    pyi_builder.test_source("import uvloop")


@importorskip('web3')
def test_web3(pyi_builder):
    pyi_builder.test_source("import web3")


@importorskip('phonenumbers')
def test_phonenumbers(pyi_builder):
    pyi_builder.test_source("""
        import phonenumbers

        number = '+17034820623'
        parsed_number = phonenumbers.parse(number)

        assert(parsed_number.country_code == 1)
        assert(parsed_number.national_number == 7034820623)
        """)


@importorskip('pendulum')
def test_pendulum(pyi_builder):
    pyi_builder.test_source("""
        import pendulum

        print(pendulum.now().isoformat())
        """)


@importorskip('humanize')
def test_humanize(pyi_builder):
    pyi_builder.test_source("""
        import humanize
        from datetime import timedelta

        print(humanize.naturaldelta(timedelta(seconds=125)))
        """)


@importorskip('argon2')
def test_argon2(pyi_builder):
    pyi_builder.test_source("""
        from argon2 import PasswordHasher

        ph = PasswordHasher()
        hash = ph.hash("s3kr3tp4ssw0rd")
        ph.verify(hash, "s3kr3tp4ssw0rd")
        """)


@importorskip('pytest')
def test_pytest_runner(pyi_builder):
    """
    Check if pytest runner builds correctly.
    """
    pyi_builder.test_source(
        """
        import pytest
        import sys
        sys.exit(pytest.main(['--help']))
        """)


@importorskip('eel')
def test_eel(pyi_builder):
    pyi_builder.test_source("import eel")


@importorskip('sentry_sdk')
def test_sentry(pyi_builder):
    pyi_builder.test_source(
        """
        import sentry_sdk
        sentry_sdk.init()
        """)


@importorskip('iminuit')
def test_iminuit(pyi_builder):
    pyi_builder.test_source("""
        from iminuit import Minuit
        """)


@importorskip('av')
def test_av(pyi_builder):
    pyi_builder.test_source("""
        import av
        """)


@importorskip('passlib')
@xfail(is_linux and is_py39 and not is_module_satisfies('passlib > 1.7.4'),
       reason='Passlib does not account for crypt() behavior change that '
              'was introduced in 3.9.x (python #39289).')
def test_passlib(pyi_builder):
    pyi_builder.test_source("""
        import passlib.apache
        """)


@importorskip('publicsuffix2')
def test_publicsuffix2(pyi_builder):
    pyi_builder.test_source("""
        import publicsuffix2
        publicsuffix2.PublicSuffixList()
        """)


@importorskip('pydivert')
def test_pydivert(pyi_builder):
    pyi_builder.test_source("""
        import pydivert
        pydivert.WinDivert.check_filter("inbound")
        """)


@importorskip('statsmodels')
@pytest.mark.skipif(not is_module_satisfies('statsmodels >= 0.12'),
                    reason='This has only been tested with statsmodels >= 0.12.')
def test_statsmodels(pyi_builder):
    pyi_builder.test_source("""
        import statsmodels.api as sm
        """)


@importorskip('win32ctypes')
@pytest.mark.skipif(not is_win, reason='pywin32-ctypes is supported only on Windows')
@pytest.mark.parametrize('submodule', ['win32api', 'win32cred', 'pywintypes'])
def test_pywin32ctypes(pyi_builder, submodule):
    pyi_builder.test_source(f"""
        from win32ctypes.pywin32 import {submodule}
        """)


@importorskip('pyproj')
@pytest.mark.skipif(not is_module_satisfies('pyproj >= 2.1.3'),
                    reason='The test supports only pyproj >= 2.1.3.')
def test_pyproj(pyi_builder):
    pyi_builder.test_source("""
        import pyproj
        tf = pyproj.Transformer.from_crs(
            7789,
            8401
        )
        result = tf.transform(
            xx=3496737.2679,
            yy=743254.4507,
            zz=5264462.9620,
            tt=2019.0
        )
        print(result)
        """)


@importorskip('pydantic')
def test_pydantic(pyi_builder):
    pyi_builder.test_source("""
        import datetime
        import pprint

        import pydantic


        class User(pydantic.BaseModel):
            id: int
            name: str = 'John Doe'
            signup_ts: datetime.datetime


        external_data = {'id': 'not an int', }
        try:
            User(**external_data)
        except pydantic.ValidationError as e:
            pprint.pprint(e.errors())
        """)


@requires('google-api-python-client >= 2.0.0')
def test_googleapiclient(pyi_builder):
    pyi_builder.test_source("""
        from googleapiclient import discovery, discovery_cache

        API_NAME = "youtube"
        API_VERSION = "v3"

        for file in os.listdir(discovery_cache.DISCOVERY_DOC_DIR): # Always up to date
            if file.startswith("youtube.v") and file.endswith(".json"):
                API_NAME, API_VERSION = file.split(".")[:2]
                break

        # developerKey can be any non-empty string
        yt = discovery.build(API_NAME, API_VERSION, developerKey=":)", static_discovery=True)
        """)


@importorskip('eth_typing')
def test_eth_typing(pyi_builder):
    pyi_builder.test_source("""
        import eth_typing
    """)


@importorskip("eth_utils")
def test_eth_utils_network(pyi_builder):
    pyi_builder.test_source("""
        import eth_utils.network
        eth_utils.network.name_from_chain_id(1)
    """)


@importorskip('plotly')
@importorskip('pandas')
def test_plotly(pyi_builder):
    pyi_builder.test_source("""
        import pandas as pd
        import plotly.express as px

        data = [(1, 1), (2, 1), (3, 5), (4, -3)]
        df = pd.DataFrame.from_records(data, columns=['col_1', 'col_2'])
        fig = px.scatter(df, x='col_1', y='col_2')
        """)


@pytest.mark.timeout(600)
@importorskip('dash')
def test_dash(pyi_builder):
    pyi_builder.test_source("""
        import dash
        from dash.dependencies import Input, Output

        app = dash.Dash(__name__)
        app.layout = dash.html.Div(
            [
                dash.dcc.Input(id='input_text', type='text', placeholder='input type text'),
                dash.html.Div(id='out-all-types'),
            ]
        )

        @app.callback(
            Output('out-all-types', 'children'),
            [Input('input_text', 'value')],
        )
        def cb_render(val):
            return val
        """)


@importorskip('dash')
def test_dash_table(pyi_builder):
    pyi_builder.test_source("""
        import dash

        app = dash.Dash(__name__)
        app.layout = dash.dash_table.DataTable(
            id='table',
            columns=[{'name': 'a', 'id': 'a'}, {'name': 'b', 'id': 'b'}],
            data=[{'a': 1, 'b': 2}, {'a': 3, 'b': 4}],
        )
        """)


@importorskip('dash')
@importorskip('dash_bootstrap_components')
def test_dash_bootstrap_components(pyi_builder):
    pyi_builder.test_source("""
        import dash
        import dash_bootstrap_components as dbc

        app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
        alert = dbc.Alert([dash.html.H4('Well done!', className='alert-heading')])
        """)


@importorskip('blspy')
def test_blspy(pyi_builder):
    pyi_builder.test_source("""
        import blspy
        """)


@importorskip('flirpy')
def test_flirpy(pyi_builder):
    pyi_builder.test_source("""
        from flirpy.camera.lepton import Lepton

        print(Lepton.find_video_device())
        """)


@importorskip('office365')
def test_office365(pyi_builder):
    pyi_builder.test_source("""
        from office365.runtime.auth.providers.saml_token_provider import SamlTokenProvider

        provider = SamlTokenProvider("https://example.com", "bob", "bob's password", "")
        parameters = dict.fromkeys(["auth_url", "message_id", "username", "password", "created", "expires",
                                    "issuer", "serviceTokenUrl", "assertion_node"], "")

        provider._prepare_request_from_template("FederatedSAML.xml", parameters)
        provider._prepare_request_from_template("RST2.xml", parameters)
        provider._prepare_request_from_template("SAML.xml", parameters)
        """)


@importorskip('thinc')
def test_thinc(pyi_builder):
    pyi_builder.test_source("""
        from thinc.backends import numpy_ops
        """)


@importorskip('srsly')
def test_srsly(pyi_builder):
    pyi_builder.test_source("""
        import srsly
        """)


@importorskip('spacy')
def test_spacy(pyi_builder):
    pyi_builder.test_source("""
        import spacy
        """)


@importorskip('shotgun_api3')
def test_shotgun_api3(pyi_builder):
    pyi_builder.test_source("""
        import shotgun_api3
        """)


@importorskip('msoffcrypto')
def test_msoffcrypto(pyi_builder):
    pyi_builder.test_source("""
        import msoffcrypto
        """)


@importorskip('mariadb')
def test_mariadb(pyi_builder):
    pyi_builder.test_source("""
        import mariadb
        """)


@importorskip('dash_uploader')
def test_dash_uploader(pyi_builder):
    pyi_builder.test_source("""
        import dash_uploader
        """)


@importorskip('cloudscraper')
def test_cloudscraper(pyi_builder):
    pyi_builder.test_source("""
        import cloudscraper
        scraper = cloudscraper.create_scraper()
        """)


@importorskip('mnemonic')
def test_mnemonic(pyi_builder):
    pyi_builder.test_source("""
        import mnemonic
        mnemonic.Mnemonic("english")
        """)


@importorskip('pynput')
def test_pynput(pyi_builder):
    pyi_builder.test_source("""
        import pynput
        """)


@importorskip('pystray')
def test_pystray(pyi_builder):
    pyi_builder.test_source("""
        import pystray
        """)


@importorskip('rtree')
def test_rtree(pyi_builder):
    pyi_builder.test_source("""
        import rtree
        """)


@importorskip('pingouin')
def test_pingouin(pyi_builder):
    pyi_builder.test_source("""
        import pingouin
        """)


@importorskip('timezonefinder')
def test_timezonefinder(pyi_builder):
    pyi_builder.test_source("""
        from timezonefinder import TimezoneFinder
        TimezoneFinder()
        """)


@importorskip('uvicorn')
def test_uvicorn(pyi_builder):
    pyi_builder.test_source("""
        from uvicorn import lifespan, loops
        """)


@importorskip("langdetect")
def test_langdetect(pyi_builder):
    pyi_builder.test_source("""
        import langdetect
        print(langdetect.detect("this is a test"))
        """)


@importorskip("swagger_spec_validator")
def test_swagger_spec_validator(pyi_builder):
    pyi_builder.test_source("""
        from swagger_spec_validator.common import read_resource_file
        read_resource_file("schemas/v1.2/resourceListing.json")
        read_resource_file("schemas/v2.0/schema.json")
        """)


@requires('pythonnet < 3.dev')
@pytest.mark.skipif(not is_win, reason='pythonnet 2 does not support .Net Core, so its only supported by Windows')
def test_pythonnet2(pyi_builder):
    pyi_builder.test_source("""
        import clr
        """)


@requires('pythonnet >= 3.dev')
def test_pythonnet3(pyi_builder):
    pyi_builder.test_source("""
        from clr_loader import get_coreclr
        from pythonnet import set_runtime
        set_runtime(get_coreclr())  # Pick up and use any installed .NET runtime.

        import clr
        """)


if is_win:
    # This is a hack to prevent monkeypatch from interfering with PyQt5's additional PATH entries. See:
    # https://github.com/pyinstaller/pyinstaller/commit/b66c9021129e9e875ddd138a298ce542483dd6c9
    try:
        import PyQt5  # noqa: F401
    except ImportError:
        pass


@importorskip("qtmodern")
@importorskip("PyQt5")
def test_qtmodern(pyi_builder):
    pyi_builder.test_source("""
        import sys
        from PyQt5 import QtWidgets
        import qtmodern.styles
        import qtmodern.windows

        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QWidget()
        qtmodern.styles.dark(app)
        modern_window = qtmodern.windows.ModernWindow(window)
        modern_window.show()
        """)


@importorskip("platformdirs")
def test_platformdirs(pyi_builder):
    pyi_builder.test_source("""
        import platformdirs
        platformdirs.user_data_dir("FooApp", "Mr Foo")
        """)


@importorskip("websockets")
def test_websockets(pyi_builder):
    pyi_builder.test_source("import websockets")


@importorskip("tableauhyperapi")
def test_tableauhyperapi(pyi_builder):
    pyi_builder.test_source("""
        import tableauhyperapi
        """)


@importorskip("pymssql")
def test_pymssql(pyi_builder):
    pyi_builder.test_source("""
        import pymssql
        """)


@importorskip("branca")
def test_branca(pyi_builder):
    pyi_builder.test_source("""
        import branca
        """)


@importorskip("folium")
def test_folium(pyi_builder):
    pyi_builder.test_source("""
        import folium
        m = folium.Map(location=[0, 0], zoom_start=5)
        """)


@importorskip("comtypes")
@pytest.mark.skipif(not is_win, reason="comtypes is Windows only")
def test_comtypes_stream(pyi_builder):
    pyi_builder.test_source("""
        import pathlib
        import sys
        import comtypes.client

        module = comtypes.client.GetModule("shdocvw.dll")

        try:
            pathlib.Path(module.__file__).relative_to(sys._MEIPASS)
            raise SystemExit(f"Error: comtypes is writing inside the application: {module.__file__}")
        except ValueError:
            pass
    """)


@importorskip("metpy")
def test_metpy(pyi_builder):
    # Import metpy.plots, which triggers search for colortables data.
    pyi_builder.test_source("""
        import metpy.plots
        """)


@importorskip("pyvjoy")
def test_pyvjoy(pyi_builder):
    pyi_builder.test_source("""
        import pyvjoy
        """)


@importorskip("adbutils")
def test_adbutils(pyi_builder):
    # adbutils 0.15.0 renamed adbutils._utils.get_adb_exe() to adb_path()
    if is_module_satisfies("adbutils >= 0.15.0"):
        pyi_builder.test_source("""
            from adbutils._utils import adb_path; adb_path()
            """)
    else:
        pyi_builder.test_source("""
            from adbutils._utils import get_adb_exe; get_adb_exe()
            """)


@importorskip("apkutils")
def test_apkutils(pyi_builder):
    pyi_builder.test_source("""
        from apkutils import APK
    """)


@importorskip("pymediainfo")
def test_pymediainfo(pyi_builder):
    pyi_builder.test_source("""
        from pymediainfo import MediaInfo
        MediaInfo._get_library()  # Trigger search for shared library.
        """)


@importorskip("sacremoses")
def test_sacremoses(pyi_builder):
    pyi_builder.test_source("""
        import sacremoses
        """)


@importorskip("pypeteer")
def test_pypeteer(pyi_builder):
    pyi_builder.test_source("""
        import pypeteer
        print(pypeteer.version)
        """)


@importorskip("tzdata")
@pytest.mark.skipif(not is_py39 and not can_import_module('importlib_resources'),
                    reason='importlib_resources is required on python < 3.9.')
def test_tzdata(pyi_builder):
    pyi_builder.test_source("""
        import tzdata.zoneinfo  # hiddenimport

        try:
            import importlib.resources as importlib_resources
        except ImportError:
            import importlib_resources

        # This emulates time-zone data retrieval from tzdata, as peformed by
        # zoneinfo / backports.zoneinfo
        zone_name = "Europe/Ljubljana"

        components = zone_name.split("/")
        package_name = ".".join(["tzdata.zoneinfo"] + components[:-1])
        resource_name = components[-1]

        with importlib_resources.open_binary(package_name, resource_name) as fp:
            data = fp.read()

        print(data)
        """)


@importorskip("backports.zoneinfo")
@pytest.mark.skipif(is_win and not can_import_module('tzdata'),
                    reason='On Windows, backports.zoneinfo requires tzdata.')
def test_backports_zoneinfo(pyi_builder):
    pyi_builder.test_source("""
        from backports import zoneinfo
        tz = zoneinfo.ZoneInfo("Europe/Ljubljana")
        print(tz)
        """)


@importorskip("zoneinfo")
@pytest.mark.skipif(is_win and not can_import_module('tzdata'),
                    reason='On Windows, zoneinfo requires tzdata.')
def test_zoneinfo(pyi_builder):
    pyi_builder.test_source("""
        import zoneinfo
        tz = zoneinfo.ZoneInfo("Europe/Ljubljana")
        print(tz)
        """)


@importorskip("panel")
def test_panel(pyi_builder):
    pyi_builder.test_source("""
        import panel

        # Load the Ace extension to trigger lazy-loading of model
        panel.extension("ace")
        """)


@importorskip("pandas_flavor")
def test_pandas_flavor(pyi_builder):
    pyi_builder.test_source("""
        from pandas_flavor import register_dataframe_accessor

        @register_dataframe_accessor("dummy")
        class DummyAccessor:
            pass
    """)


@importorskip("pyviz_comms")
def test_pyviz_comms(pyi_builder):
    pyi_builder.test_source("""
        import pyviz_comms
        """)


@importorskip("pyphen")
def test_pyphen(pyi_builder):
    pyi_builder.test_source("""
        import pyphen
        """)


@importorskip("pandas")
@importorskip("plotly")
@importorskip("kaleido")
def test_kaleido(pyi_builder):
    pyi_builder.test_source("""
        import plotly.express as px
        fig = px.scatter(px.data.iris(), x="sepal_length", y="sepal_width", color="species")
        fig.write_image("figure.png", engine="kaleido")
        """)


@pytest.mark.skipif(is_win,
                    reason='On Windows, Cairo dependencies cannot be installed using Chocolatey.')
@importorskip("cairocffi")
def test_cairocffi(pyi_builder):
    pyi_builder.test_source("""
        import cairocffi
        """)


@pytest.mark.skipif(is_win,
                    reason='On Windows, Cairo dependencies cannot be installed using Chocolatey.')
@importorskip("cairosvg")
def test_cairosvg(pyi_builder):
    pyi_builder.test_source("""
        import cairosvg
        """)


@importorskip("ffpyplayer")
def test_ffpyplayer(pyi_builder):
    pyi_builder.test_source("""
        import ffpyplayer.player
        """)


@importorskip("cv2")
def test_cv2(pyi_builder):
    pyi_builder.test_source("""
        import cv2
        """)


# Requires OpenCV with enabled HighGUI
@importorskip("cv2")
def test_cv2_highgui(pyi_builder):
    from PyInstaller import isolated

    @isolated.decorate
    def _get_cv2_highgui_backend():
        import re
        import cv2

        # Find `GUI: <type>` line in OpenCV build information dump. This is available only in recent OpenCV versions;
        # in earlier versions, we would need to parse all subsequent backend entries, which is out of our scope here.
        pattern = re.compile(r'$\s*GUI\s*:\s*(?P<gui>\S+)\s*^', re.MULTILINE)
        info = cv2.getBuildInformation()
        m = pattern.search(info)
        if not m:
            return None

        return m.group('gui')

    has_gui = True
    backend = _get_cv2_highgui_backend()
    if backend is None:
        # We could not determine the backend from OpenCV information; fall back to the dist name
        if is_module_satisfies('opencv-python-headless'):
            has_gui = False
    elif backend == "NONE":
        has_gui = False

    if not has_gui:
        pytest.skip("OpenCV has no GUI support.")

    pyi_builder.test_source("""
        import cv2
        import numpy as np

        img = np.zeros((64, 64), dtype='uint8')
        cv2.imshow("Test", img)
        cv2.waitKey(1000)  # Wait a second
        """)


@importorskip("twisted")
def test_twisted_default_reactor(pyi_builder):
    pyi_builder.test_source("""
        from twisted.internet import reactor
        assert callable(reactor.listenTCP)
        """)


@importorskip("twisted")
def test_twisted_custom_reactor(pyi_builder):
    pyi_builder.test_source("""
        import sys
        if sys.platform.startswith("win") and sys.version_info >= (3,7):
            import asyncio
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        from twisted.internet import asyncioreactor
        asyncioreactor.install()
        from twisted.internet import reactor
        assert callable(reactor.listenTCP)
        """)


@importorskip("pygraphviz")
def test_pygraphviz_bundled_programs(pyi_builder):
    # Test that the frozen application is using collected graphviz executables instead of system-installed ones.
    pyi_builder.test_source("""
        import sys
        import os
        import pygraphviz

        bundle_dir = os.path.normpath(sys._MEIPASS)
        dot_path = os.path.normpath(pygraphviz.AGraph()._get_prog('dot'))

        assert os.path.commonprefix([dot_path, bundle_dir]) == bundle_dir, \
            f"Invalid program path: {dot_path}!"
        """)


@importorskip("pygraphviz")
def test_pygraphviz_functional(pyi_builder, tmp_path):
    # Functional test for pygraphviz that tries to use different programs and output formats to ensure that graphviz
    # programs and plugins are properly collected.
    pyi_builder.test_source("""
        import sys
        import os
        import pygraphviz as pgv

        output_dir = sys.argv[1] if len(sys.argv) >= 2 else '.'

        print("Setting up graph...")
        G = pgv.AGraph(strict=False, directed=True)

        # Set default node attributes
        G.graph_attr["label"] = "Name of graph"
        G.node_attr["shape"] = "circle"
        G.edge_attr["color"] = "red"

        G.add_node("a")
        G.add_edge("b", "c")  # add edge (and the nodes)

        print("Dumping graph to string...")
        s = G.string()
        print(s)

        print("Test layout with default program (= neato)")
        G.layout()

        print("Test layout with 'dot' program")
        G.layout(prog="dot")

        print("Writing previously positioned graph to PNG file...")
        G.draw(os.path.join(output_dir, "file.png"))

        print("Using 'circo' to position, writing PS file...")
        G.draw(os.path.join(output_dir, "file.ps"), prog="circo")

        print("Done!")
        """, app_args=[str(tmp_path)])


@importorskip("pypsexec")
def test_pypsexec(pyi_builder):
    pyi_builder.test_source("""
        from pypsexec.paexec import paexec_out_stream
        next(paexec_out_stream())
        """)


@importorskip("mimesis")
def test_mimesis(pyi_builder):
    pyi_builder.test_source("""
        from mimesis import Address
        Address().address()
        """)


@importorskip('orjson')
def test_orjson(pyi_builder):
    pyi_builder.test_source("""
        import orjson
        """)


@importorskip('altair')
def test_altair(pyi_builder):
    pyi_builder.test_source("""
        import altair
        """)


@importorskip('fabric')
def test_fabric(pyi_builder):
    pyi_builder.test_source("""
        import fabric
        """)


@importorskip('cassandra')
def test_cassandra(pyi_builder):
    pyi_builder.test_source("""
        import cassandra
        """)


@importorskip('gitlab')
def test_gitlab(pyi_builder):
    pyi_builder.test_source("""
        import gitlab
        """)


@importorskip('graphql_query')
def test_graphql_query(pyi_builder):
    pyi_builder.test_source("""
        from graphql_query import Operation, Query
        hero = Query(name="hero", fields=["name"])
        operation = Operation(type="query", queries=[hero])
        print(operation.render())
        """)


@importorskip('shapely')
def test_shapely(pyi_builder):
    pyi_builder.test_source("""
        from shapely.geometry import Point
        patch = Point(0.0, 0.0).buffer(10.0)
        print(patch.area)
        """)


@importorskip('lark')
def test_lark(pyi_builder):
    pyi_builder.test_source("""
        import lark
        parser = lark.Lark('''
            value: "true"
            %import common.SIGNED_NUMBER''',
            start='value')
    """)


@importorskip('stdnum')
def test_stdnum_iban(pyi_builder):
    pyi_builder.test_source("""
        import stdnum.iban
    """)


@importorskip('numcodecs')
def test_numcodecs(pyi_builder):
    pyi_builder.test_source("""
        # numcodecs uses multiprocessing
        import multiprocessing
        multiprocessing.freeze_support()
        from numcodecs import Blosc
    """)


@importorskip('pypemicro')
def test_pypemicro(pyi_builder):
    pyi_builder.test_source("""
        from pypemicro import PyPemicro
        assert PyPemicro.get_pemicro_lib()
    """)


@importorskip('sounddevice')
def test_sounddevice(pyi_builder):
    pyi_builder.test_source("""
        import sounddevice
    """)


@importorskip('soundfile')
def test_soundfile(pyi_builder):
    pyi_builder.test_source("""
        import soundfile
    """)


@importorskip('limits')
def test_limits(pyi_builder):
    pyi_builder.test_source("""
        import limits
    """)


@pytest.mark.skipif(is_win,
                    reason='On Windows, Weasyprint dependencies cannot be installed using Chocolatey.')
@importorskip("weasyprint")
def test_weasyprint(pyi_builder):
    pyi_builder.test_source("""
        import weasyprint
        """)


@importorskip("great_expectations")
def test_great_expectations(pyi_builder):
    # Reproduce the error from pyinstaller/pyinstaller-hooks-contrib#445
    pyi_builder.test_source("""
        from great_expectations.render.view import view
        v = view.DefaultJinjaView()
        """)


@importorskip('pyshark')
def test_pyshark(pyi_builder):
    pyi_builder.test_source(
        """
        import pyshark
        #capture = pyshark.FileCapture('/tmp/networkpackages.cap')
        #data = [print x for x in capture]
        #print(data)
        """
    )


@importorskip('PyQt5')
@importorskip('pyqtgraph')
def test_pyqtgraph(pyi_builder):
    pyi_builder.test_source(
        """
        import pyqtgraph.graphicsItems.PlotItem
        import pyqtgraph.graphicsItems.ViewBox.ViewBoxMenu
        import pyqtgraph.imageview.ImageView
        """
    )


@importorskip('PyQt5')
@importorskip('pyqtgraph')
def test_pyqtgraph_colormap(pyi_builder):
    pyi_builder.test_source(
        """
        import pyqtgraph.colormap
        assert pyqtgraph.colormap.listMaps()
        """
    )


@importorskip('PyQt5')
@importorskip('pyqtgraph')
def test_pyqtgraph_remote_graphics_view(pyi_builder):
    pyi_builder.test_source(
        """
        import sys
        import os
        import signal

        from PyQt5 import QtCore, QtWidgets
        import pyqtgraph

        # Multiprocessing is used internally by pyqtgraph.multiprocess
        import multiprocessing
        multiprocessing.freeze_support()

        # pyqtgraph.multiprocess also uses a subprocess.Popen() to spawn its
        # sub-process, so we need to restore _MEIPASS2 to prevent the executable
        # to unpacking itself again in the subprocess.
        os.environ['_MEIPASS2'] = sys._MEIPASS

        # Create a window with remote graphics view
        app = QtWidgets.QApplication(sys.argv)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        window = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(window)
        remote_view = pyqtgraph.widgets.RemoteGraphicsView.RemoteGraphicsView()
        layout.addWidget(remote_view)

        window.show()

        # Quit after a second
        QtCore.QTimer.singleShot(1000, app.exit)

        sys.exit(app.exec_())
        """
    )


@importorskip('hydra')
def test_hydra(pyi_builder):
    config_file = pathlib.Path(__file__).parent / 'data' / 'test_hydra' / 'config.yaml'

    pyi_builder.test_source(
        """
        import os

        import hydra
        from omegaconf import DictConfig, OmegaConf

        config_path = os.path.join(os.path.dirname(__file__), 'conf')

        @hydra.main(config_path=config_path, config_name="config")
        def my_app(cfg):
            assert cfg.test_group.secret_string == 'secret'
            assert cfg.test_group.secret_number == 123

        if __name__ == "__main__":
            my_app()
        """,
        pyi_args=['--add-data', f"{config_file}:conf"]
    )


@importorskip('pywintypes')
def test_pywintypes(pyi_builder):
    pyi_builder.test_source("""
        import pywintypes
        """)


@importorskip('pythoncom')
def test_pythoncom(pyi_builder):
    pyi_builder.test_source("""
        import pythoncom
        """)


@importorskip('spiceypy')
def test_spiceypy(pyi_builder):
    pyi_builder.test_source("""
        import spiceypy
    """)


@importorskip('discid')
def test_discid(pyi_builder):
    pyi_builder.test_source(
        """
        # Basic import check
        import discid

        # Check that shared library is in fact collected into application bundle.
        # We expect the hook to collect it to top-level directory (sys._MEIPASS).
        import discid.libdiscid
        lib_name = discid.libdiscid._LIB_NAME

        lib_file = os.path.join(sys._MEIPASS, lib_name)
        assert os.path.isfile(lib_file), f"Shared library {lib_name} not collected to _MEIPASS!"
        """
    )


@importorskip('exchangelib')
def test_exchangelib(pyi_builder):
    pyi_builder.test_source("""
        import exchangelib
    """)


@importorskip('cftime')
def test_cftime(pyi_builder):
    pyi_builder.test_source("""
        import cftime
    """)


@importorskip('netCDF4')
def test_netcdf4(pyi_builder):
    pyi_builder.test_source("""
        import netCDF4
    """)


@importorskip('charset_normalizer')
def test_charset_normalizer(pyi_builder):
    pyi_builder.test_source("""
        import base64
        import charset_normalizer
        message = base64.b64decode(b"yUCEmYWBlIWEQIFAhJmFgZRAloZAgUCUlpmFQKKFlaKJgpOFQJeBg5KBh4U=")
        print(charset_normalizer.from_bytes(message).best())
    """)


@importorskip('cf_units')
def test_cf_units(pyi_builder):
    pyi_builder.test_source("""
        import cf_units
    """)


@importorskip('compliance_checker')
def test_compliance_checker(pyi_builder):
    # The test file - taken from the package's own test data/examples. Use an .nc file instead of .cdl one, because
    # loading the latter requires ncgen utility to be available on the system.
    pkg_path = get_module_attribute('compliance_checker', '__path__')[0]
    input_file = pathlib.Path(pkg_path) / 'tests' / 'data' / 'bad-trajectory.nc'
    assert input_file.is_file(), f"Selected test file, {input_file!s} does not exist! Fix the test!"

    pyi_builder.test_source("""
        import os
        import json

        import compliance_checker
        import compliance_checker.runner

        input_file = sys.argv[1]

        # Load all available checker classes
        check_suite = compliance_checker.runner.CheckSuite()
        check_suite.load_all_available_checkers()

        # Run cf and adcc checks
        return_value, errors = compliance_checker.runner.ComplianceChecker.run_checker(
            input_file,
            checker_names=['cf', 'acdd'],
            verbose=False,
            criteria='normal',
            output_filename='-',
            output_format='json')

        # We do not really care about validation results, just that validation finished without raising any exceptions.
        print("Return value:", return_value)
        print("Errors occurred:", errors)
    """, app_args=[str(input_file)])


@importorskip('nbt')
def test_nbt(pyi_builder):
    pyi_builder.test_source("""
        import nbt
    """)


@importorskip('minecraft_launcher_lib')
def test_minecraft_launcher_lib(pyi_builder):
    pyi_builder.test_source(
        '''
        import minecraft_launcher_lib
        assert isinstance(minecraft_launcher_lib.utils.get_library_version(), str)
        '''
    )


@importorskip('moviepy')
def test_moviepy(pyi_builder):
    # `moviepy.editor` tries to access the `moviepy.video.fx` and `moviepy.audio.fx` plugins/modules via the
    # `moviepy.video.fx.all` and `moviepy.video.fx.all` modules, which in turn programmatically import and
    # forward all corresponding submodules.
    #
    # `moviepy.editor` was removed in moviepy 2.x, and now all imports go through `moviepy`. The `moviepy.video.fx.all`
    # and `moviepy.video.fx.all` modules with their programmatic imports seem to be gone as well... So turn this into
    # a basic import test with 2.x series.
    if is_module_satisfies('moviepy >= 2.0.0'):
        pyi_builder.test_source("""
            import moviepy
        """)
    else:
        pyi_builder.test_source("""
            import moviepy.editor
        """)


@importorskip('customtkinter')
def test_customtkinter(pyi_builder):
    pyi_builder.test_source("""
        import customtkinter
    """)


@importorskip('pylibmagic')
def test_pylibmagic(pyi_builder):
    pyi_builder.test_source("""
        import pylibmagic
        import os
        import sys

        bundle_dir = os.path.normpath(sys._MEIPASS)
        pylibmagic_data_path = f"{bundle_dir}/pylibmagic"

        files_to_assert = ["magic.mgc"]
        if sys.platform == 'darwin':
            files_to_assert.append("libmagic.1.dylib")
        elif sys.platform.startswith('linux'):
            files_to_assert.append("libmagic.so.1")

        for file in files_to_assert:
            assert os.path.isfile(f"{pylibmagic_data_path}/{file}"), \
                f"The {file} was not collected to _MEIPASS!"
    """)


@importorskip('fastparquet')
def test_fastparquet(pyi_builder):
    pyi_builder.test_source("""
        import fastparquet
    """)


@importorskip('librosa')
def test_librosa(pyi_builder):
    pyi_builder.test_source("""
        import librosa

        # Requires intervals.msgpack data file
        import librosa.core.intervals

        # Requires example files on import
        import librosa.util.files
    """)


@importorskip('librosa')
def test_librosa_util_function(pyi_builder):
    # Test that functions from `librosa.util` that use `numba` vectorization can be run in frozen application.
    pyi_builder.test_source("""
        import librosa.util
        import numpy as np

        x = np.array([1, 0, 1, 2, -1, 0, -2, 1])
        result = librosa.util.localmin(x)
        expected = np.array([False,  True, False, False,  True, False,  True, False])
        assert (result == expected).all()
    """)


@importorskip('sympy')
def test_sympy(pyi_builder):
    pyi_builder.test_source("""
        import sympy
    """)


@importorskip('bokeh')
def test_bokeh(pyi_builder):
    pyi_builder.test_source("""
        import bokeh
    """)


@importorskip('xyzservices')
def test_xyzservices(pyi_builder):
    pyi_builder.test_source("""
        import xyzservices.providers
        print(xyzservices.providers.CartoDB)
    """)


@importorskip('mistune')
def test_mistune(pyi_builder):
    pyi_builder.test_source("""
        import mistune
    """)


@importorskip('jsonschema')
def test_jsonschema(pyi_builder):
    pyi_builder.test_source("""
        import jsonschema

        # Sample schema
        schema = {
            "type" : "object",
            "properties" : {
                "price" : {"type" : "number"},
                "name" : {"type" : "string"},
            },
        }

        jsonschema.validate(instance={"name" : "Eggs", "price" : 3.38}, schema=schema)

        try:
            jsonschema.validate(instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema)
        except jsonschema.ValidationError as e:
            print(f"Validation error: {e}")
    """)


@importorskip('psutil')
def test_psutil(pyi_builder):
    pyi_builder.test_source("""
        import psutil
    """)


@importorskip('litestar')
def test_litestar(pyi_builder):
    pyi_builder.test_source("""
        from litestar import Litestar, get
        from litestar.testing import TestClient
        from typing import Dict, Any


        @get("/sync", sync_to_thread=False)
        def sync_hello_world() -> Dict[str, Any]:
            return {"hello": "world"}


        app = Litestar(route_handlers=[sync_hello_world])
        client = TestClient(app)
        response = client.get("/sync")
        assert response.status_code == 200
        assert response.json() == {"hello": "world"}
    """)


@importorskip('lingua')
def test_lingua_language_detector(pyi_builder):
    pyi_builder.test_source("""
        from lingua import Language, LanguageDetectorBuilder

        languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
        detector = LanguageDetectorBuilder.from_languages(*languages).build()

        assert detector.detect_language_of("languages are awesome") == Language.ENGLISH
    """)


@importorskip('opencc')
def test_opencc(pyi_builder):
    pyi_builder.test_source("""
        import opencc

        cc = opencc.OpenCC('s2t')

        assert cc.convert('开放中文转换') == '開放中文轉換'
    """)


@importorskip('jieba')
def test_jieba(pyi_builder):
    pyi_builder.test_source("""
        import jieba

        assert jieba.lcut('我来到北京清华大学') == ['我', '来到', '北京', '清华大学']
    """)


@importorskip('simplemma')
def test_simplemma(pyi_builder):
    pyi_builder.test_source("""
        import simplemma

        assert simplemma.lemmatize('tests', lang='en') == 'test'
    """)


@importorskip('wordcloud')
def test_wordcloud(pyi_builder):
    pyi_builder.test_source("""
        import wordcloud

        wordcloud.WordCloud().generate('test')
    """)


@importorskip('eng_to_ipa')
def test_eng_to_ipa(pyi_builder):
    pyi_builder.test_source("""
        import eng_to_ipa
    """)


@importorskip('mecab')
def test_mecab(pyi_builder):
    pyi_builder.test_source("""
        import mecab

        mecab.MeCab()
    """)


@importorskip('khmernltk')
def test_khmernltk(pyi_builder):
    pyi_builder.test_source("""
        import khmernltk
    """)


@importorskip('pycrfsuite')
def test_pycrfsuite(pyi_builder):
    pyi_builder.test_source("""
        import pycrfsuite
    """)


@importorskip('pymorphy3')
def test_pymorphy3(pyi_builder):
    # Language availability depends on installed packages.
    available_languages = []
    if can_import_module('pymorphy3_dicts_ru'):
        available_languages.append('ru')
    if can_import_module('pymorphy3_dicts_uk'):
        available_languages.append('uk')

    pyi_builder.test_source("""
        import sys
        import pymorphy3

        languages = sys.argv[1:]
        print(f"Languages to test: {languages}")

        for language in languages:
            pymorphy3.MorphAnalyzer(lang=language)
    """, app_args=available_languages)


@importorskip('sudachipy')
@importorskip('sudachidict_small')
@importorskip('sudachidict_core')
@importorskip('sudachidict_full')
def test_sudachipy(pyi_builder):
    pyi_builder.test_source("""
        from sudachipy import Dictionary

        Dictionary(dict='small').create()
        Dictionary(dict='core').create()
        Dictionary(dict='full').create()
    """)


@importorskip('laonlp')
def test_laonlp(pyi_builder):
    pyi_builder.test_source("""
        import laonlp
    """)


@importorskip('pythainlp')
def test_pythainlp(pyi_builder):
    pyi_builder.test_source("""
        import pythainlp
    """)


@importorskip('gmsh')
def test_gmsh(pyi_builder):
    pyi_builder.test_source("""
        import gmsh
    """)


@importorskip('sspilib')
def test_sspilib(pyi_builder):
    pyi_builder.test_source("""
        import sspilib

        cred = sspilib.UserCredential(
            "username@DOMAIN.COM",
            "password",
        )

        ctx = sspilib.ClientSecurityContext(
            credential=cred,
            target_name="host/server.domain.com",
        )

        print(ctx)
    """)


@importorskip('rlp')
def test_rlp(pyi_builder):
    pyi_builder.test_source("""
        import rlp
    """)


@importorskip('eth_rlp')
def test_eth_rlp(pyi_builder):
    pyi_builder.test_source("""
        import eth_rlp
    """)


@importorskip('z3c.rml')
def test_z3c_rml_rml2pdf(pyi_builder):
    pyi_builder.test_source("""
        from z3c.rml import rml2pdf

        rml = '''
        <!DOCTYPE document SYSTEM "rml.dtd" >
        <document filename="test.pdf">
          <template showBoundary="1">
            <!--Debugging is now turned on, frame outlines -->
            <!--will appear on the page -->
            <pageTemplate id="main">
              <!-- two frames are defined here: -->
              <frame id="first" x1="100" y1="400" width="150" height="200" />
              <frame id="second" x1="300" y1="400" width="150" height="200" />
            </pageTemplate>
          </template>
          <stylesheet><!-- still empty...--></stylesheet>
          <story>
            <para>Welcome to RML.</para>
          </story>
        </document>
        '''

        pdf_bytes = rml2pdf.parseString(rml)
    """)


@importorskip('freetype')
def test_pyi_freetype(pyi_builder):
    pyi_builder.test_source("""
        import sys
        import pathlib

        import freetype

        # Ensure that the freetype shared library is bundled with the frozen application; otherwise, freetype might be
        # using system-wide library.

        # First, check that freetype.FT_Library_filename is an absolute path; otherwise, it is likely using
        # basename-only ctypes fallback.
        ft_library_file = pathlib.Path(freetype.FT_Library_filename)
        print(f"FT library file (original): {ft_library_file}", file=sys.stderr)
        assert ft_library_file.is_absolute(), "FT library file is not an absolute path!"

        # Check that fully-resolved freetype.FT_Library_filename is anchored in fully-resolved frozen application
        # directory.
        app_dir = pathlib.Path(__file__).resolve().parent
        print(f"Application directory: {app_dir}", file=sys.stderr)
        ft_library_path = pathlib.Path(ft_library_file).resolve()
        print(f"FT library file (resolved): {ft_library_path}", file=sys.stderr)
        assert app_dir in ft_library_path.parents, "FT library is not bundled with frozen application!"
    """)


@importorskip('vaderSentiment')
def test_vadersentiment(pyi_builder):
    pyi_builder.test_source("""
        import vaderSentiment.vaderSentiment
        vaderSentiment.vaderSentiment.SentimentIntensityAnalyzer()
    """)


@importorskip('langchain')
def test_langchain_llm_summarization_checker(pyi_builder):
    pyi_builder.test_source("""
        import langchain.chains.llm_summarization_checker.base
    """)


@importorskip('seedir')
def test_seedir(pyi_builder):
    pyi_builder.test_source("""
        import seedir
    """)


@importorskip('PyTaskbar')
@pytest.mark.skipif(not is_win, reason='PyTaskbar is supported only on Windows')
def test_PyTaskbar(pyi_builder):
    pyi_builder.test_source("""
            import PyTaskbar
        """)


@importorskip('celpy')
def test_celpy(pyi_builder):
    pyi_builder.test_source("""
        import celpy
    """)


@importorskip('pygwalker')
def test_pygwalker(pyi_builder):
    pyi_builder.test_source("""
        import pygwalker
    """)


@importorskip('pypylon')
def test_pypylon(pyi_builder):
    pyi_builder.test_source("""
        from pypylon import pylon
    """)


@importorskip('osgeo')
def test_osgeo(pyi_builder):
    pyi_builder.test_source("""
        from osgeo import osr
        sr = osr.SpatialReference()
        sr.ImportFromEPSG(4326)
        assert(sr.EPSGTreatsAsLatLong())
    """)


@importorskip('falcon')
def test_falcon(pyi_builder):
    # https://github.com/falconry/falcon/blob/v3.1.3/examples/things.py
    pyi_builder.test_source("""
        import falcon
    """)


@importorskip('iso639')
def test_iso639(pyi_builder):
    pyi_builder.test_source("""
        from iso639 import Lang
        test = Lang("en")
    """)


# Basic JIT test with numba
@importorskip('numba')
def test_numba_jit(pyi_builder):
    pyi_builder.test_source("""
        import numba

        @numba.jit
        def f(x, y):
            return x + y

        assert f(1, 2) == 3
    """)


# Basic import test with new type system enabled (numba >= 0.61).
# Ideally, we would repeat the above `test_numba_jit`, but at the time of writing (numba 0.61.0rc2) it does not seem to
# work even when unfrozen.
@importorskip('numba')
@pytest.mark.skipif(not is_module_satisfies('numba >= 0.61.0rc1'), reason="Requires numba >= 0.61.0.")
def test_numba_new_type_system(pyi_builder):
    pyi_builder.test_source("""
        import os
        os.environ['NUMBA_USE_LEGACY_TYPE_SYSTEM'] = '0'
        import numba
    """)


# Check that `numba.cloudpickle.cloudpickle_fast` is collected even if it is not directly imported anywhere.
@importorskip('numba')
def test_numba_cloudpickle_fast(pyi_builder):
    pyi_builder.test_source("""
        # Assume the application or its dependencies import numba somewhere.
        import numba

        # Simulate indirect import of `numba.cloudpickle.cloudpickle_fast`that would happen during data unpickling.
        import importlib
        modname = "numba.cloudpickle.cloudpickle_fast"
        mod = importlib.import_module(modname)
    """)


# Check that `cloudpickle.cloudpickle_fast` is collected even if it is not directly imported anywhere.
@importorskip('cloudpickle')
def test_cloudpickle_fast(pyi_builder):
    pyi_builder.test_source("""
        # Assume the application or its dependencies import cloudpickle somewhere.
        import cloudpickle

        # Simulate indirect import of `cloudpickle.cloudpickle_fast`that would happen during data unpickling.
        import importlib
        modname = "cloudpickle.cloudpickle_fast"
        mod = importlib.import_module(modname)
    """)


# Check if pptx template is included
@importorskip('pptx')
def test_pptx(pyi_builder):
    pyi_builder.test_source("""
        import pptx
        pptx.Presentation()
    """)


@importorskip('opentelemetry.sdk')
def test_opentelemetry(pyi_builder):
    # Basic tracer example, taken from
    # https://github.com/open-telemetry/opentelemetry-python/blob/main/docs/examples/basic_tracer/basic_trace.py
    pyi_builder.test_source("""
        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import (
            BatchSpanProcessor,
            ConsoleSpanExporter,
        )

        trace.set_tracer_provider(TracerProvider())
        trace.get_tracer_provider().add_span_processor(
            BatchSpanProcessor(ConsoleSpanExporter())
        )
        tracer = trace.get_tracer(__name__)
        with tracer.start_as_current_span("foo"):
            print("Hello world!")
    """)


# Basic test for cryptography package
@importorskip('cryptography')
def test_cryptography(pyi_builder):
    pyi_builder.test_source("""
        from cryptography.fernet import Fernet

        key = Fernet.generate_key()
        f = Fernet(key)

        token = f.encrypt(b"This is test.")
        print(f"Encrypted message: {token}")

        print(f"Decrypted message: {f.decrypt(token)}")
    """)


@importorskip('xarray')
def test_xarray(pyi_builder):
    pyi_builder.test_source("""
        import xarray as xr
        import numpy as np

        data = xr.DataArray(
            np.random.randn(2, 3),
            dims=("x", "y"),
            coords={"x": [10, 20]},
        )
        print(data)
    """)


# Shows that we need to collect `xarray.chunkmanagers` entry point.
# See: https://github.com/pyinstaller/pyinstaller/issues/8786
@importorskip('xarray')
@importorskip('dask')  # requires dask for default 'dask' chunk manager to become available
def test_xarray_chunk(pyi_builder):
    pyi_builder.test_source("""
        import xarray as xr
        import numpy as np

        v = xr.Variable(dims=("T",), data=np.random.randn(10)).chunk()
    """)


# Test that we can import `dask.array` when `jinja2` is also available. In this case, `dask.array.core` ends up loading
# template files from `dask.widgets.templates`. Requires `numpy` (or `dask[array]`) for `dask.array` to be importable,
# and `jinja2` (`dask[diagnostics]`) for template files to become mandatory.
@importorskip('dask')
@importorskip('jinja2')
@importorskip('numpy')
def test_dask_array(pyi_builder):
    pyi_builder.test_source("""
        import dask.array
    """)


# Basic test for dask's `distributed` package, based on quickstart example from their documentation.
@importorskip('distributed')
def test_dask_distributed(pyi_builder):
    pyi_builder.test_source("""
        import multiprocessing
        from dask.distributed import Client

        def process():
            client = Client()

            def square(x):
                return x ** 2

            def neg(x):
                return -x

            A = client.map(square, range(10))
            B = client.map(neg, A)

            total = client.submit(sum, B)
            return total.result()

        if __name__ == '__main__':
            multiprocessing.freeze_support()
            result = process()
            assert result == -285
    """)


@importorskip('tables')
def test_pytables(pyi_builder):
    # NOTE: run_from_path=True prevents `pyi_builder` from completely clearing the `PATH` environment variable. At the
    # time of writing, `cpu_info` (used by PyTables) raises error if `PATH` is missing from `os.environ`.
    pyi_builder.test_source("""
        # `tables` uses cpu_info package during initialization, which in turn uses `multiprocessing`, so we need to call
        # `multiprocessing.freeze_support()` before importing `tables`.
        import multiprocessing
        multiprocessing.freeze_support()

        import tables
    """, run_from_path=True)


@importorskip('schwifty')
def test_schwifty(pyi_builder):
    pyi_builder.test_source("""
        import schwifty

        iban = schwifty.IBAN('DE89 3704 0044 0532 0130 00')
        print(iban.country_code)
        print(iban.bank_code)
        print(iban.account_code)
    """)


@importorskip('eccodes')
def test_eccodes_gribapi(pyi_builder):
    pyi_builder.test_source("""
        import sys
        import os
        import pathlib

        # With eccodes 2.37.0, eccodes needs to be imported before gribapi to avoid circular imports.
        import eccodes

        # Basic import test
        import gribapi

        # Ensure that the eccodes shared library is bundled with the frozen application.
        import gribapi.bindings

        print(f"gribapi.bindings.library_path={gribapi.bindings.library_path}")

        library_path = gribapi.bindings.library_path
        if os.path.basename(library_path) == library_path:
            # Only library basename is given - assume this is a system-wide copy that was collected
            # into top-level application directory and loaded via `findlibs.find()`/`ctypes`.
            expected_library_file = os.path.join(
                sys._MEIPASS,
                library_path,
            )
            if not os.path.isfile(expected_library_file):
                raise RuntimeError(f"Shared library {expected_library_file!s} not found!")
        else:
            # Absolute path; check that it is rooted in top-level application directory. This covers all valid locations
            # as per https://github.com/ecmwf/eccodes-python/blob/2.37.0/gribapi/bindings.py#L61-L64,
            #  - sys._MEIPASS/eccodes
            #  - sys._MEIPASS/eccodes.libs
            #  - sys._MEIPASS/eccodes/.dylibs
            # as well as sys._MEIPASS itself (in case system-wide copy was collected into top-level application
            # directory but is reported with full path instead of just basename due to our override of `findlibs.find()`
            # via run-time hook).
            if pathlib.PurePath(sys._MEIPASS) not in pathlib.PurePath(library_path).parents:
                raise RuntimeError(
                    f"Shared library path {library_path} is not rooted in top-level application directory!"
                )
    """)


@importorskip('dbus_fast')
def test_dbus_fast(pyi_builder):
    pyi_builder.test_source("""
        import os
        import sys
        import asyncio
        import json

        from dbus_fast import Message, MessageType
        from dbus_fast.aio import MessageBus


        async def main():
            # Connect to bus
            try:
                bus = await MessageBus().connect()
            except Exception as e:
                print(f"Could not connect to bus: {e}")
                return

            # List all available names
            reply = await bus.call(
                Message(
                    destination="org.freedesktop.DBus",
                    path="/org/freedesktop/DBus",
                    interface="org.freedesktop.DBus",
                    member="ListNames",
                )
            )

            if reply.message_type == MessageType.ERROR:
                raise Exception(reply.body[0])

            print(json.dumps(reply.body[0], indent=2))


        asyncio.run(main())
    """)


@importorskip('patoolib')
def test_patoolib(pyi_builder):
    pyi_builder.test_source("""
        import patoolib

        archive = 'archive.zip'

        # The call to `get_archive_cmdlist_func` triggers import of module from `patoolib.programs` via
        # `importlib.import_module`; the set up below is based on code from `patoolib._extract_archive`.
        archive_format, compression = patoolib.get_archive_format(archive)
        print(f"Archive format: {archive_format}")
        print(f"Compression: compression")

        program = patoolib.find_archive_program(archive_format, 'extract')
        print(f"Program: {program}")

        cmdlist = patoolib.get_archive_cmdlist_func(program, 'extract', archive_format)
        print(f"Cmdlist: {cmdlist}")
    """)


@importorskip('cmocean')
def test_cmocean(pyi_builder):
    pyi_builder.test_source("""
        import cmocean
    """)


@importorskip('tzwhere')
def test_tzwhere(pyi_builder):
    pyi_builder.test_source("""
        from tzwhere import tzwhere
        tzwhere.tzwhere()
    """)


@importorskip('pydicom')
def test_pydicom(pyi_builder):
    pyi_builder.test_source("""
        import pydicom
    """)


@importorskip('pyexcel_ods')
def test_pyexcel_ods(pyi_builder):
    pyi_builder.test_source("""
        import pyexcel_ods
    """)


@importorskip('itk')
def test_itk(pyi_builder):
    pyi_builder.test_source("""
        import itk
    """)


@importorskip('slixmpp')
def test_slixmpp(pyi_builder):
    pyi_builder.test_source("""
        import slixmpp
        slixmpp.ClientXMPP('username', 'password')
    """)


@importorskip('capstone')
def test_capstone(pyi_builder):
    pyi_builder.test_source("""
        import capstone
        capstone.__version__
    """)


@importorskip('yapf')
def test_yapf(pyi_builder):
    pyi_builder.test_source("""
        import yapf
    """)


@importorskip('grapheme')
def test_grapheme(pyi_builder):
    pyi_builder.test_source("""
        import grapheme
    """)


@importorskip('xmlschema')
def test_xmlschema(pyi_builder):
    pyi_builder.test_source("""
        import xmlschema
    """)


@importorskip('saml2')
def test_saml2(pyi_builder):
    pyi_builder.test_source("""
        # this loads XSD files
        import saml2.xml.schema

        # this loads submodules from saml2.attributemap
        from saml2.attribute_converter import ac_factory
        ac_factory()
    """)


# The prerequisite for this test is that tkinter can be used unfrozen, so try instantiating a window in a subprocess
# to verify that this is the case. This check should cover the following scenarios:
#  - tkinter missing
#  - import of tkinter crashes python interpreter
#  - tkinter.Tk() fails due to DISPLAY not being set on linux
#  - tkinter.Tk() fails due to faulty build (e.g., due to Tcl/Tk version mix-up, as seen with python <= 3.10 builds on
#    macos-12 GHA runners; https://github.com/actions/setup-python/issues/649#issuecomment-1745056485)
def _tkinter_fully_usable():
    from PyInstaller import isolated

    @isolated.decorate
    def _create_tkinter_window():
        import tkinter
        tkinter.Tk()

    try:
        _create_tkinter_window()
    except Exception:
        return False

    return True


@importorskip('sv_ttk')
def test_sv_ttk(pyi_builder):
    if not _tkinter_fully_usable():
        pytest.skip("tkinter is not fully usable.")
    pyi_builder.test_source("""
        import sv_ttk

        # Initialize sv_ttk to ensure it works correctly
        sv_ttk.set_theme("dark")
    """)


@importorskip('tkinterdnd2')
def test_tkinterdnd2(pyi_builder):
    if not _tkinter_fully_usable():
        pytest.skip("tkinter is not fully usable.")
    pyi_builder.test_source("""
        import tkinter
        import tkinterdnd2

        root = tkinterdnd2.TkinterDnD.Tk()

        list_box = tkinter.Listbox(root)
        list_box.insert(1, "drag files here")

        list_box.drop_target_register(tkinterdnd2.DND_FILES)
        list_box.dnd_bind('<<Drop>>', lambda e: list_box.insert(tkinter.END, e.data))

        list_box.pack()

        def shutdown_timer_callback():
            print("Shutting down!")
            root.destroy()

        shutdown_interval = 1000  # ms
        print(f"Starting shutdown timer ({shutdown_interval} ms)...")
        root.after(shutdown_interval, shutdown_timer_callback)

        print("Entering main loop...")
        root.mainloop()

        print("Done!")
    """)


@importorskip('toga')
def test_toga(pyi_builder):
    pyi_builder.test_script(
        "pyi_toga_app.py",
        app_args=['--automatic-shutdown', '5'],
        pyi_args=['--windowed'] if is_darwin else [],
    )


@importorskip('numbers_parser')
def test_numbers_parser(pyi_builder, tmp_path):
    output_filename = tmp_path / "output.numbers"
    pyi_builder.test_source("""
        import sys
        import numbers_parser

        output_filename = sys.argv[1]

        doc = numbers_parser.Document()
        doc.add_sheet("New Sheet", "New Table")
        sheet = doc.sheets["New Sheet"]
        table = sheet.tables["New Table"]
        table.write(1, 1, 1000)
        table.write(1, 2, 2000)
        table.write(1, 3, 3000)
        doc.save(output_filename)
    """, app_args=[str(output_filename)])


@importorskip('fsspec')
def test_fsspec_protocols(pyi_builder, tmp_path):
    # Get the list of working protocols in unfrozen python
    @isolated.decorate
    def _get_working_fsspec_protocols():
        import fsspec

        working_protocols = []
        for protocol in fsspec.available_protocols():
            try:
                fsspec.get_filesystem_class(protocol)
                working_protocols.append(protocol)
            except ImportError:
                pass
            except Exception:
                # Work around for fsspec/filesystem_spec#1805
                pass

        return sorted(working_protocols)

    protocols_unfrozen = _get_working_fsspec_protocols()
    print(f"Unfrozen protocols: {protocols_unfrozen}")

    assert protocols_unfrozen, "No working protocols found!"

    # Obtain list of working protocols in frozen application.
    output_file = tmp_path / "output.txt"

    pyi_builder.test_source("""
        import sys
        import fsspec

        working_protocols = []
        for protocol in fsspec.available_protocols():
            try:
                obj = fsspec.get_filesystem_class(protocol)
                working_protocols.append(protocol)
            except ImportError:
                pass
            except Exception:
                # Work-around for fsspec/filesystem_spec#1805
                pass

        with open(sys.argv[1], 'w') as fp:
            for protocol in working_protocols:
                print(f"{protocol}", file=fp)
    """, app_args=[str(output_file)])

    with open(output_file, "r") as fp:
        protocols_frozen = sorted(line.strip() for line in fp)
    print(f"Frozen protocols: {protocols_frozen}")

    assert protocols_frozen == protocols_unfrozen


@importorskip('zarr')
@importorskip('xarray')
def test_xarray_to_zarr(pyi_builder):
    pyi_builder.test_source("""
        import xarray as xr
        import numpy as np

        data = xr.DataArray(
            np.random.randn(2, 3),
            dims=("x", "y"),
            coords={"x": [10, 20]},
        )
        data_zarr = data.to_zarr()
        print(data)
    """)


@importorskip('intake')
def test_intake(pyi_builder):
    pyi_builder.test_source("""
        import intake

        print(f"intake version: {intake.__version__}")
        catalog = intake.Catalog()
    """)


@importorskip('intake')
def test_intake_plugins(pyi_builder, tmp_path):
    # Get the list of plugins in unfrozen python
    @isolated.decorate
    def _get_intake_plugins():
        import intake
        return sorted(list(intake.registry))

    plugins_unfrozen = _get_intake_plugins()
    print(f"Unfrozen plugins: {plugins_unfrozen}")

    # Obtain list of plugins in frozen application.
    output_file = tmp_path / "output.txt"

    pyi_builder.test_source("""
        import sys
        import intake

        with open(sys.argv[1], 'w') as fp:
            for plugin in intake.registry:
                print(f"{plugin}", file=fp)
    """, app_args=[str(output_file)])

    with open(output_file, "r") as fp:
        plugins_frozen = sorted(line.strip() for line in fp)
    print(f"Frozen plugins: {plugins_frozen}")

    assert plugins_frozen == plugins_unfrozen


@importorskip('h3')
def test_h3(pyi_builder):
    pyi_builder.test_source("""
        import h3
    """)


@importorskip('selectolax')
def test_selectolax(pyi_builder):
    pyi_builder.test_source("""
        import selectolax
    """)


@importorskip('ruamel.yaml')
@pytest.mark.skipif(
    not is_module_satisfies('ruamel.yaml.string'),
    reason='ruamel.yaml.string plugin is not installed',
)
def test_ruamel_yaml_string_plugin(pyi_builder):
    pyi_builder.test_source("""
        import ruamel.yaml

        yaml = ruamel.yaml.YAML(typ=['rt', 'string'])
        data  = dict(abc=42, help=['on', 'its', 'way'])
        print(yaml.dump_to_string(data))
    """)


@importorskip('pypdfium2')
def test_pypdfium2(pyi_builder):
    pyi_builder.test_source("""
        import pypdfium2
    """)


@importorskip('dateutil')
def test_dateutil(pyi_builder):
    pyi_builder.test_source("""
        from dateutil.zoneinfo import getzoneinfofile_stream

        assert getzoneinfofile_stream()
    """)


@importorskip('niquests')
def test_niquests(pyi_builder):
    pyi_builder.test_source("""
        import niquests

        try:
            with niquests.Session() as s:
                s.get("http://tarpit/timeout", timeout=0.001)
        except (niquests.ConnectionError, niquests.Timeout):
            pass

        try:
            with niquests.Session(disable_http1=True) as s:
                s.get("http://tarpit/timeout", timeout=0.001)
        except (niquests.ConnectionError, niquests.Timeout):
            pass

        try:
            with niquests.Session(disable_http1=True, disable_http2=True) as s:
                s.get("https://tarpit/timeout", timeout=0.001)
        except (niquests.ConnectionError, niquests.Timeout):
            pass

        try:
            with niquests.Session() as s:
                s.get("sse://tarpit/timeout", timeout=0.001)
        except (niquests.ConnectionError, niquests.Timeout):
            pass
    """)


@importorskip('emoji')
def test_emoji(pyi_builder):
    pyi_builder.test_source("""
        import emoji
    """)


# Basic test for urllib3 - either from urllib3 or urllib3-future
@importorskip('urllib3')
def test_urllib3(pyi_builder):
    pyi_builder.test_source("""
        import urllib3

        http = urllib3.PoolManager()
        try:
            resp = http.request("GET", "https://localhost/robots.txt")
        except urllib3.exceptions.HTTPError:
            pass
    """)


# Basic test for urllib3_future from urllib3-future
@importorskip('urllib3_future')
def test_urllib3_future(pyi_builder):
    pyi_builder.test_source("""
        import urllib3_future

        http = urllib3_future.PoolManager()
        try:
            resp = http.request("GET", "https://localhost/robots.txt")
        except urllib3_future.exceptions.HTTPError:
            pass
    """)


@importorskip('black')
def test_black(pyi_builder):
    pyi_builder.test_source("""
        import black

        mode = black.Mode(
            target_versions=set(),  # auto-detect
            line_length=120,
        )

        code = "print ('hello, world') "
        print("Original code: {code!r}")

        reformatted_code = black.format_file_contents(
            code,
            fast=False,
            mode=mode,
        )
        print("Reformatted code: {code!r}")

        # Try reformatting again - this should raise black.NothingChanged
        try:
            reformatted_code2 = black.format_file_contents(
                reformatted_code,
                fast=False,
                mode=mode,
            )
        except black.NothingChanged:
            pass
        else:
            raise RuntimeError("black.NothingChanged exception was not raised!")
    """)


@importorskip('blib2to3')
def test_black_blib2to3_pygram(pyi_builder):
    pyi_builder.test_source("""
        import blib2to3.pygram
    """)


@importorskip('blib2to3')
def test_black_blib2to3_pytree(pyi_builder):
    pyi_builder.test_source("""
        import blib2to3.pytree
    """)


@importorskip('frictionless')
def test_frictionless(pyi_builder, tmp_path):
    # Example CSV file, taken from upstream example at
    # https://framework.frictionlessdata.io/docs/getting-started.html
    csv_file = tmp_path / "example.csv"
    csv_file.write_text("\n".join([
        "id,name,,name"
        "1,english"
        "1,english"
        ""
        "2,german,1,2,3"
    ]))

    pyi_builder.test_source("""
        import sys
        import pprint

        import frictionless

        filename = sys.argv[1]

        # frictionless.describe()
        print("Testing frictionless.describe...")
        output = frictionless.describe(filename)
        pprint.pprint(output)

        # frictionless.extract()
        print("Testing frictionless.extract...")
        output = frictionless.extract(filename)
        pprint.pprint(output)

        # frictionless.validate()
        print("Testing frictionless.validate...")
        output = frictionless.validate(filename)
        pprint.pprint(output)
    """, app_args=[str(csv_file)])


@importorskip('pandas')
@importorskip('pandera')
def test_pandera(pyi_builder):
    # Example from pandera's Quick Start
    pyi_builder.test_source("""
        import pandas as pd
        import pandera as pa

        # data to validate
        df = pd.DataFrame({
            "column1": [1, 4, 0, 10, 9],
            "column2": [-1.3, -1.4, -2.9, -10.1, -20.4],
            "column3": ["value_1", "value_2", "value_3", "value_2", "value_1"]
        })

        # define schema
        schema = pa.DataFrameSchema({
            "column1": pa.Column(int, checks=pa.Check.le(10)),
            "column2": pa.Column(float, checks=pa.Check.lt(-1.2)),
            "column3": pa.Column(str, checks=[
                pa.Check.str_startswith("value_"),
                # define custom checks as functions that take a series as input and
                # outputs a boolean or boolean Series
                pa.Check(lambda s: s.str.split("_", expand=True).shape[1] == 2)
            ]),
        })

        validated_df = schema(df)
        print(validated_df)
    """)


@importorskip('tkinterweb')
def test_tkinterweb(pyi_builder):
    pyi_builder.test_source("""
        import tkinter
        import tkinterweb

        root = tkinter.Tk()
        frame = tkinterweb.HtmlFrame(root, messages_enabled=False)

        # Load a test string that uses all files that should have been bundled
        frame.load_html(
                            "<img src='this path doesn't exist' alt='Hello, World!'/> \
                            <p>Hello Again!</p> \
                            <select><option>Hi...</option></select>"
                            )
    """)


@importorskip('tkinterweb_tkhtml')
def test_tkinterweb_tkhtml(pyi_builder):
    pyi_builder.test_source("""
        import tkinter
        import tkinterweb_tkhtml

        root = tkinter.Tk()

        folder = tkinterweb_tkhtml.get_tkhtml_folder()
        tkinterweb_tkhtml.load_tkhtml(root, folder)

        frame = tkinter.Widget(root, "html")

        # Load a test string
        frame.tk.call(frame._w, "parse", "<p>Hello, World!</p>")
    """)


@importorskip('narwhals')
def test_narwhals(pyi_builder):
    pyi_builder.test_source("""
        import narwhals
    """)


@importorskip('pynng')
def test_pynng(pyi_builder):
    pyi_builder.test_source("""
        import pynng
    """)


@importorskip('uuid6')
def test_uuid6(pyi_builder):
    pyi_builder.test_source("""
        import uuid6

        my_uuid = uuid6.uuid6()
        print(my_uuid)
        assert my_uuid < uuid6.uuid6()
    """)
