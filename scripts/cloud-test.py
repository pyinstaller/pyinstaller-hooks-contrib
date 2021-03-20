#!/usr/bin/env python
# -----------------------------------------------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# -----------------------------------------------------------------------------------------------------------
"""
A command line interface to launch the 'Oneshot test' workflow (.github/workflows/oneshot-test.yml).
"""

import os
from pathlib import Path
import subprocess
import re
from pprint import pformat
import textwrap

try:
    import click
    import github

except ImportError:
    raise SystemExit("The script requires PyGithub and click. Please run the following then re-run this script\n\n"
                     "pip install click PyGithub\n")


HERE = Path(__file__).parent


def authenticated_user():
    """Get a logged in Github user."""
    # Anyone know a better way of doing this?
    token = os.environ.get("GITHUB_TOKEN")

    if token is None:
        token = input("Please enter a Github authentication token or your username and password separated by a space.\n"
                      "Alternatively you may set the GITHUB_TOKEN environment variable instead:\n")

    user = github.Github(*token.split(maxsplit=1))
    try:
        user.get_user().login
    except github.BadCredentialsException:
        raise SystemExit("Authentication failed due to invalid credentials.")

    print("Authenticated successfully.")
    return user


def _get_current_branch():
    """Get the branch currently active locally in git.

    The location of this repo is defined based on the location of this script so it is current-working-dir
    independent.
    """
    branch_command = ["git", "-C", str(HERE), "branch"]
    branch_output = subprocess.check_output(branch_command).decode()
    return re.search(r"\*\s*(\S+)\n", branch_output).group(1)


def launch_workflow(workflow, branch, params):
    workflow.update()
    old_len = workflow.get_runs().totalCount

    # Launch the workflow. This only returns a boolean.
    if not workflow.create_dispatch(branch, params):
        raise SystemExit("The workflow failed to launch. Check your authentication token has sufficient permissions to "
                         "use the Github API. It bizarrely requires both read and write access.")

    print("Request has been accepted. Waiting for the build to go live",
          end="")
    while old_len == workflow.get_runs().totalCount:
        print(".", end="")
        workflow.update()
    print()

    build = workflow.get_runs()[0]
    print("Tests are live at:", build.html_url)

    return build


def _norm_comma_space(x):
    """Prettify comma deliminated text to always have one space after a comma."""
    return re.sub(", *", ", ", x)


PYTHONS = ["3.5", "3.6", "3.7", "3.8"]
OSs = ["ubuntu", "windows", "macos"]


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument("package", nargs=-1)
@click.option("--py", multiple=True, default=["3.7"],
              help="Python version(s) to test on. Separate multiple versions with a comma or use this parameter "
                   "multiple times to test multiple versions. You may specify micro versions such as 3.7.9 although "
                   "this is discouraged as they are not guaranteed to be available. Use 'all' to select {}. "
                   "Defaults to '3.7'.".format(PYTHONS))
@click.option("--os", multiple=True, default=["ubuntu"], type=click.Choice(OSs + ["all"], case_sensitive=False),
              help="Which OSs to test on. Use 'all' to specify all three. Defaults to 'ubuntu'.")
@click.option("--fail-fast", default=False, is_flag=True, help="Cancel all other builds if any one of them fails.")
@click.option("--fork", default=None,
              help="Which fork of pyinstaller-hooks-contrib to use. Defaults to the fork of the authenticated user.")
@click.option("--branch", default=None,
              help="The branch to test. Defaults to using git to get your currently active branch.")
@click.option("--commands", multiple=True,
              help="Additional bash installation commands to run. Ran after setting up Python but before pip-installing"
                   "dependencies.")
@click.option("--browser", default=False, is_flag=True,
              help="Open the live build on Github in a browser window.")
@click.option("--dry-run", is_flag=True, help="Don't launch a build. Just parse and print the parameters.")
def main(package, py, os, fork, branch, fail_fast, commands, browser, dry_run):
    """Launch CI testing of a given package against multiple package or Python versions and OSs.

    The **package** specifies only those to install. Which tests should be ran is inferred implicitly by
    ``@pytest.importorskip``.

    Basic usage: Launch two jobs to test the ``pycparser`` hooks on linux, Pythons 3.6 and 3.7, using the latest
    version of ``pycparser``. And open the build in a browser window.

        python cloud-test.py --py=3.6,3.7 --os=ubuntu --browser pycparser

    The **package** can be anything you'd put on the right hand side of `pip install`. Multiple packages to install can
    be separated by a space: Launch one job which installs and tests two libraries.

        python cloud-test.py pycparser==2.10 passlib==1.7.1

    Multiple versions to be run in separate jobs should be deliminated by a comma: Launch 4 x 2 = 8 jobs to test the
    ``pycparser`` hooks on windows, with all supported Pythons, against two versions of ``pycparser``.

        python cloud-test.py --py=all --os=windows pycparser==2.20, pycparser==2.16

    When you're absolutely certain your hook is ready for it, you may test everything (please use sparingly - this costs
    Github a lot of $$$). This would create 4 x 3 x 3 = 36 jobs.

        python cloud-test.py --py=all --os=all pycparser==2.16, pycparser==2.18, pycparser==2.20

    It costs Github 10x as much to run macOS as it does Linux. So please use Ubuntu as your default OS and test macOS
    last, in conservative batches. Github Actions is free for us but it won't stay that way if we abuse it.

    """

    # --- Parse and normalise input parameters. ---

    # The bulk of the parsing is already done by the workflow. We mostly just need to serialise it into the same format
    # as the web UI.
    if any("all" in i for i in py):
        py = PYTHONS

    if "all" in os:
        os = OSs

    package = " ".join(package)

    params = {
        "python-version": _norm_comma_space(",".join(py)),
        "package": _norm_comma_space(package),
        "os": _norm_comma_space(",".join(os).lower()),
        "fail-fast": str(fail_fast).lower(),
        "commands": "; ".join(commands),
    }

    print("Configuration options to be passed to CI:")
    print(textwrap.indent(pformat(params), "    "))

    # --- Find and connect to the right workflow ---

    #  Login.
    user = authenticated_user()

    # Work out which fork we're supposed to use:
    if fork is None:
        fork = user.get_user().login

    try:
        repo = user.get_repo(fork + "/pyinstaller-hooks-contrib")
    except github.UnknownObjectException:
        raise SystemExit(
            "The repo {}/pyinstaller-hooks-contrib does not exist. Use the --fork option to specify the fork. Or, if "
            "you have adequate permissions, use --fork=pyinstaller to use the master repo.".format(fork))

    # Work out which branch we're using.
    if branch is None:
        try:
            branch = _get_current_branch()
        except subprocess.SubprocessError:
            raise SystemExit(
                "Failed to guess the branch using git. Please specify it manually using the --branch option.")

    print("Using the '{}' branch of:\n    {}".format(branch, repo.html_url))

    branch = repo.get_branch(branch)

    # Get the workflow to trigger:

    # There doesn't seem to be a better way to get a specific workflow besides
    # iterating through them until we find the right one.
    workflow = next(i for i in repo.get_workflows()
                    if i.name == "Oneshot test")

    # --- Launch the build ---

    if dry_run:
        print("Dry run only: abort")
        return

    build = launch_workflow(workflow, branch, params)

    if browser:
        import webbrowser
        webbrowser.open(build.html_url)


if __name__ == "__main__":
    main()
