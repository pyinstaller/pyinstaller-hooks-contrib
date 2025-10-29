

from PyInstaller.utils.tests import requires


@requires("nicegui >= 3.0")
def test_nicegui(pyi_builder):
    pyi_builder.test_source("""
        import asyncio
        import multiprocessing
        import os
        from contextlib import asynccontextmanager

        import httpx
        from nicegui import core, ui
        from nicegui.functions.download import download
        from nicegui.functions.navigate import Navigate
        from nicegui.functions.notify import notify
        from nicegui.testing.user_plugin import User


        async def test_button_click():
            @asynccontextmanager
            async def user_of(ui_code):
                try:
                    # simulate user and keep NiceGUI fully headless for tests
                    os.environ['NICEGUI_USER_SIMULATION'] = 'true'

                    # don't spawn reloader/native window; don't open browser
                    ui.run(ui_code, reload=False, native=False, show=False)

                    async with core.app.router.lifespan_context(core.app):
                        async with httpx.AsyncClient(
                            transport=httpx.ASGITransport(core.app),
                            base_url='http://test'
                        ) as client:
                            yield User(client)
                finally:
                    os.environ.pop('NICEGUI_USER_SIMULATION', None)
                    ui.navigate = Navigate()
                    ui.notify = notify
                    ui.download = download

            def ui_code() -> None:
                ui.button('Click me', on_click=lambda: ui.notify('Hello World!'))

            async with user_of(ui_code) as user:
                await user.open('/')
                await user.should_see('Click me')
                user.find(ui.button).click()
                await user.should_see('Hello World!')


        if __name__ == '__main__':
            multiprocessing.freeze_support()  # important for PyInstaller on Windows
            asyncio.run(test_button_click())
            print('Test passed.')
    """)
