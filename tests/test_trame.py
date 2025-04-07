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

import pytest

from PyInstaller.utils.tests import importorskip
from PyInstaller.utils.hooks import is_module_satisfies


# Pretty much all tests here require `trame.app module` from core `trame` dist, so skip the tests if it is not
# available (installing other `trame-*` dists does not seem to install `trame` dist itself). We could equivalently
# check if `trame.app` is importable, but that would require an isolated check.
pytestmark = pytest.mark.skipif(not is_module_satisfies('trame'), reason="Core 'trame' distribution is not installed.")


@importorskip("trame")
def test_trame(pyi_builder):
    pyi_builder.test_source("""
        import trame
    """)


@importorskip('trame_client')
def test_trame_client(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip('trame_vuetify')
def test_trame_vuetify(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.vuetify3 import VAppLayout


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        VAppLayout(server)
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("vtkmodules")
@importorskip("trame_vtk")
@importorskip("trame_vuetify")  # implies existence of trame.widgets.vuetify, which we need in this test.
def test_trame_vtk(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_vtk.widgets import vtk


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            vtk.VtkMesh("test")
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("pyvista")
@importorskip("vtkmodules")
@importorskip("nest_asyncio")
@importorskip("trame_vtk")
def test_trame_vtk_tools(pyi_builder, tmp_path):
    pyi_builder.test_source("""
        import os
        import sys
        from pathlib import Path

        import pyvista as pv
        import trame_vtk

        path = Path(sys.argv[-1]) / "test.html"
        plotter = pv.Plotter()
        plotter.export_html(path)  # Uses trame_vtk
        path.unlink()
    """, app_args=[tmp_path])


@importorskip("trame_xterm")
def test_trame_xterm(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_xterm.widgets import xterm


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            xterm.XTerm()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_components")
def test_trame_components(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_components.widgets import trame


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            trame.FloatCard()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_datagrid")
def test_trame_datagrid(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_datagrid.widgets import datagrid


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            datagrid.VGrid()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_tauri")
def test_trame_tauri(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_tauri.widgets import tauri


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            tauri.Dialog()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_quasar")
def test_trame_quasar(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.quasar import QLayout
        from trame_quasar.widgets import quasar


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with QLayout(server):
            quasar.QHeader()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_tweakpane")
def test_trame_tweakpane(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_tweakpane.widgets import tweakpane


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            tweakpane.Tabs()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_deckgl")
def test_trame_deckgl(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_deckgl.widgets import deckgl


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            deckgl.Deck()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_matplotlib")
def test_trame_matplotlib(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_matplotlib.widgets import matplotlib


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            matplotlib.Figure()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_vega")
def test_trame_vega(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_vega.widgets import vega


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            vega.Figure()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_vtk3d")
def test_trame_vtk3d(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_vtk3d.widgets import vtk3d


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            vtk3d.Vtk3dScene()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_markdown")
def test_trame_markdown(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_markdown.widgets import markdown


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            markdown.Markdown()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_plotly")
def test_trame_plotly(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_plotly.widgets import plotly


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            plotly.Figure()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_code")
def test_trame_code(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_code.widgets import code


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            code.Editor()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_pvui")
def test_trame_pvui(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_pvui.widgets.colormapper import Colormapper


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            Colormapper()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("vtkmodules")
@importorskip("trame_mesh_streamer")
def test_trame_mesh_streamer(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_mesh_streamer.widgets import mesh_streamer


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            mesh_streamer.ProgressiveMesh()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_formkit")
def test_trame_formkit(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_formkit.widgets import formkit


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            formkit.FormKit()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_grid")
def test_trame_grid_layout(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_grid.widgets import grid


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            grid.GridLayout()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_iframe")
def test_trame_iframe(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_iframe.widgets import iframe


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            iframe.IFrame()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_leaflet")
def test_trame_leaflet(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_leaflet.widgets import leaflet


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            leaflet.LRectangle()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_keycloak")
def test_trame_keycloak(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_keycloak.widgets import keycloak


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            keycloak.Auth()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_router")
def test_trame_router(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_router.widgets import router


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            router.RouterView()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


@importorskip("trame_rca")
@importorskip("vtkmodules")
def test_trame_rca(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_rca.widgets import rca


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            rca.StatisticsDisplay()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)


# The vtklocal package is unstable (currently broken) so no tests can be performed.


@importorskip("trame_simput")
def test_trame_simput(pyi_builder):
    pyi_builder.test_source("""
        import asyncio

        from trame.app import get_server
        from trame.ui.html import DivLayout
        from trame_simput.widgets import simput


        async def stop(*args, **kwargs):
            await server.stop()


        server = get_server()
        with DivLayout(server):
            simput.SimputItem()
        server.controller.on_server_ready.add(
            lambda *args, **kwargs: asyncio.ensure_future(stop(*args, **kwargs))
        )
        server.start(port=0, open_browser=False)
    """)
