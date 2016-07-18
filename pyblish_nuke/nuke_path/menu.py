import logging

import nuke

logging.basicConfig(level=logging.INFO)

try:
    __import__("pyblish_nuke")
    __import__("pyblish")

except ImportError as e:
    nuke.tprint("pyblish: Could not load integration: %s " % e)

else:

    import pyblish.api
    import pyblish_nuke

    # Setup integration
    pyblish_nuke.setup()

    # register default guis
    pyblish.api.register_gui("pyblish_qml")
    pyblish.api.register_gui("pyblish_lite")
