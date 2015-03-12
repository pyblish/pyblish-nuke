# Standard library
import os
import inspect
import logging
import atexit
import subprocess
import threading
import random

# Pyblish libraries
import pyblish.api

# Integration libraries
import pyblish_nuke

# Host libraries
import nuke

log = logging.getLogger('pyblish')

cached_process = None

CREATE_NO_WINDOW = 0x08000000


def show(console=False, prefer_cached=True):
    """Show the Pyblish graphical user interface
    An interface may already have been loaded; if that's the
    case, we favour it to launching a new unless `prefer_cached`
    is False.
    """

    if cached_process and prefer_cached:
        return _show_cached()
    return _show_new(console)


def _show_cached():
    """Display cached gui
    A GUI is cached upon first being shown, or when pre-loaded.
    """

    import pyblish_endpoint.client

    pyblish_endpoint.client.request("show")

    return cached_process


def _show_new(console=False):
    """Create and display a new instance of the Pyblish QML GUI"""
    try:
        port = os.environ["ENDPOINT_PORT"]
    except KeyError:
        raise ValueError("Pyblish start-up script doesn't seem to "
                         "have been run, could not find the PORT variable")

    pid = os.getpid()
    kwargs = dict(args=["python", "-m", "pyblish_qml",
                        "--port", port, "--pid", pid])

    if not console and os.name == "nt":
        kwargs["creationflags"] = CREATE_NO_WINDOW

    log.info("Creating a new instance of Pyblish QML")
    proc = subprocess.Popen(**kwargs)

    global cached_process
    cached_process = proc

    return proc


def setup(preload=True):
    """Setup integration
    Registers Pyblish for Nuke plug-ins and appends an item to the File-menu
    """

    register_plugins()

    try:
        port = setup_endpoint()

        if preload:
            pid = os.getpid()
            preload_(port, pid)

    except:
        log.info("pyblish: Running headless")

    add_to_filemenu()

    log.info("pyblish: Integration loaded..")


def register_plugins():
    # Register accompanying plugins
    package_path = os.path.dirname(pyblish_nuke.__file__)
    plugin_path = os.path.join(package_path, 'plugins')

    pyblish.api.register_plugin_path(plugin_path)
    log.info("Registered %s" % plugin_path)


def setup_endpoint():
    """Start Endpoint
    Raises:
        ImportError: If Pyblish Endpoint is not available
    """

    from service import NukeService
    from pyblish_endpoint import server

    port = random.randint(6000, 7000)
    server.start_async_production_server(service=NukeService, port=port)
    os.environ["ENDPOINT_PORT"] = str(port)

    log.info("pyblish: Endpoint running @ %i" % port)

    return port


def preload_(port, pid=None):
    pid = os.getpid()

    kwargs = dict(args=[where('python'), "-m", "pyblish_qml",
                        "--port", str(port), "--pid", str(pid),
                        "--preload"])

    if os.name == "nt":
        kwargs["creationflags"] = CREATE_NO_WINDOW

    proc = subprocess.Popen(**kwargs)

    global cached_process
    cached_process = proc

    return proc


def is_executable(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)


def where(program):
    """Parse PATH for executables

    Windows note:
        PATHEXT yields possible suffixes, such as .exe, .bat and .cmd

    Usage:
        >>> where("python")
        c:\python27\python.exe

    """

    suffixes = [""]

    try:
        # Append Windows suffixes, such as .exe, .bat and .cmd
        suffixes.extend(os.environ.get("PATHEXT").split(os.pathsep))
    except:
        pass

    for path in os.environ["PATH"].split(os.pathsep):

        # A path may be empty.
        if not path:
            continue

        for suffix in suffixes:
            full_path = os.path.join(path, program + suffix)
            if os.path.isfile(full_path):
                return full_path


def filemenu_publish():
    """Add Pyblish to file-menu
    """

    try:
        import pyblish_nuke.lib
        pyblish_nuke.lib.show()
    except Exception as e:
        sys.stderr.write("Tried launching GUI, but failed.\n")
        sys.stderr.write("Message was: %s\n" % e)
        sys.stderr.write("Publishing in headless mode instead.\n")

        import publish.main
        pyblish.main.publish_all()


def add_to_filemenu():
    """
    """
    menubar = nuke.menu('Nuke')
    menu = menubar.menu('File')

    menu.addSeparator(index=8)

    cmd = 'import pyblish_nuke.lib;pyblish_nuke.lib.filemenu_publish()'
    menu.addCommand('Publish', cmd, index=9)

    cmd = 'import pyblish.main;pyblish.main.validate_all()'
    menu.addCommand('Validate', cmd, index=10)
