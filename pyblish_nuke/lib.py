# Standard library
import os
import inspect
import logging

# Pyblish libraries
import pyblish.api

# Integration libraries
import pyblish_nuke

# Host libraries
import nuke

log = logging.getLogger('pyblish')

def register_plugins():
    # Register accompanying plugins
    package_path = os.path.dirname(pyblish_nuke.__file__)
    plugin_path = os.path.join(package_path, 'plugins')

    pyblish.api.register_plugin_path(plugin_path)
    log.info("Registered %s" % plugin_path)


def add_to_filemenu():
    """
    """
    menubar = nuke.menu('Nuke')
    m = menubar.menu('File')

    m.addSeparator(index=6)
    m.addCommand('Publish', 'pyblish.main.publish_all()', index=7)
    m.addCommand('Validate', 'pyblish.main.validate_all()', index=8)
    m.addSeparator(index=9)