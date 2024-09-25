import sys
import argparse

import toga


class TestApp(toga.App):
    def __init__(self, *args, automatic_shutdown=0, **kwargs):
        # Hack: on macOS, toga assumes that the only possible build type is .app bundle, and tries to fall back to .app
        # bundles icon instead of default. So until this is fixed on toga's side, we need to explicitly specify the icon
        # if we are running in a POSIX build.
        if getattr(sys, "frozen", False) and sys.platform == 'darwin':
            is_app_bundle = (
                sys._MEIPASS.endswith("Contents/Frameworks") or  # PyInstaller >= 6.0
                sys._MEIPASS.endswith("Contents/MacOS")  # < PyInstaller < 6.0
            )
            if not is_app_bundle:
                print("Explicitly specifying icon for macOS POSIX build...")
                kwargs["icon"] = toga.icons.Icon.DEFAULT_ICON

        super().__init__(*args, **kwargs)
        self._automatic_shutdown = automatic_shutdown

    def startup(self):
        print("Building application UI...", file=sys.stderr)

        # Create simple UI with label and a button
        box = toga.Box()
        box.style.update(direction=toga.style.pack.COLUMN, padding=10)

        label = toga.Label("Hello world!", style=toga.style.pack.Pack(text_align=toga.style.pack.CENTER))
        box.add(label)

        button = toga.Button("Test button", on_press=self.on_button_press)
        box.add(button)

        self.main_window = toga.MainWindow()
        self.main_window.content = box
        self.main_window.show()

    def on_button_press(self, widget):
        print("Button pressed!", file=sys.stderr)

    def on_running(self):
        print("Application running!", file=sys.stderr)

        # Schedule automatic shutdown
        if self._automatic_shutdown > 0:
            print(f"Requesting shut down in {self._automatic_shutdown:.2f} seconds...", file=sys.stderr)
            self.loop.call_later(self._automatic_shutdown, self.request_exit)

    def on_exit(self):
        print("Application is about to exit!", file=sys.stderr)
        return True


def main():
    parser = argparse.ArgumentParser(description='Test application.')
    parser.add_argument(
        '--automatic-shutdown',
        metavar='seconds',
        type=float,
        default=0,
        help='Automatically shut down the application after specified number of seconds.',
    )
    args = parser.parse_args()

    app = TestApp("Test app", "org.pyinstaller.toga.test-app", automatic_shutdown=args.automatic_shutdown)
    print("Entering main loop...", file=sys.stderr)
    app.main_loop()
    print("Exited main loop", file=sys.stderr)


if __name__ == "__main__":
    main()
