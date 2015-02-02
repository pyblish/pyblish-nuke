import os
import random
import logging
import threading
import subprocess
import atexit

import nuke

GUI = None


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


def show(console=False):

    if not GUI:
        raise ValueError("No GUI registered")

    if not "ENDPOINT_PORT" in os.environ:
        raise ValueError("Pyblish start-up script doesn't seem to "
                         "have been run, could not find the PORT variable")

    host = "Nuke"
    port = os.environ["ENDPOINT_PORT"]

    CREATE_NO_WINDOW = 0x08000000
    proc = subprocess.Popen([where('python'), "-m", "pyblish_qml.app",
                             "--port", str(port)])

    # Kill child process on Nuke exit
    def kill_child():
        proc.kill()

    atexit.register(kill_child)


def setup():
    """Setup integration"""

    if has_endpoint() and has_frontend():
        setup_endpoint()
        setup_frontend()
        add_to_filemenu()
        print "pyblish: Setting up frontend"
    else:
        pass


def has_endpoint():
    try:
        __import__("pyblish_endpoint.server")
        __import__("pyblish_endpoint.service")
    except ImportError:
        return False
    return True


def has_frontend():
    try:
        __import__("pyblish_qml")
    except ImportError:
        return False
    return True


def setup_endpoint():
    from . import service

    import pyblish_endpoint.server
    import pyblish_endpoint.service

    # Listen for externally running interfaces
    port = random.randint(6000, 7000)

    def server():
        pyblish_endpoint.server.start_production_server(
            service=service.NukeService,
            port=port)

    worker = threading.Thread(target=server)
    worker.daemon = True
    worker.start()

    # Store reference to port for frontend(s)
    os.environ["ENDPOINT_PORT"] = str(port)

    nuke.tprint("pyblish: Endpoint running @ %i" % port)


def setup_frontend():
    register_gui("pyblish_qml")


def register_gui(gui):
    """Register GUI

    Inform Maya that there is a GUI for Pyblish.

    Arguments:
        gui (str): Name of callable python package/module

    """

    assert isinstance(gui, basestring)
    global GUI
    GUI = gui


def add_to_filemenu():
    menubar = nuke.menu('Nuke')
    menu = menubar.menu('File')

    menu.removeItem('Publish')
    submenu = menu.addMenu('Publish', index=7)

    cmd = 'import pyblish.main;pyblish.main.publish_all()'
    submenu.addCommand('Publish', cmd)

    cmd = 'import pyblish_nuke.frontend;pyblish_nuke.frontend.show()'
    submenu.addCommand('Publish UI', cmd)
