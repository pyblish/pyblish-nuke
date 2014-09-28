try:
    import pyblish_nuke.lib
except ImportError:
    raise ImportError("Couldn't find pyblish_nuke on your PYTHONPATH")

# Register Nuke plugins upon startup
pyblish_nuke.lib.register_plugins()
pyblish_nuke.lib.add_to_filemenu()
