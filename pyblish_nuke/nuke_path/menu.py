import logging

import nuke

logging.basicConfig(level=logging.DEBUG)

try:
    __import__("pyblish_nuke")

except ImportError as e:
    nuke.tprint("pyblish: Could not load integration: %s " % e)

else:

    import pyblish_nuke.lib
    import pyblish_nuke.frontend

    # Setup integration
    pyblish_nuke.lib.setup()

    # Setup frontend
    pyblish_nuke.frontend.setup()
