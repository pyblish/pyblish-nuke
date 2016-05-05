import logging

import nuke

try:
    __import__("pyblish_nuke")

except ImportError as e:
    nuke.tprint("pyblish: Could not load integration: %s " % e)

else:

    import pyblish_nuke.lib

    # Setup integration
    pyblish_nuke.lib.setup()
