import logging

import nuke

logging.basicConfig(level=logging.INFO)

try:
    __import__("pyblish_nuke")
    __import__("pyblish")

    # Do not load integration in NukeStudio, Hiero or HieroPlayer
    invalid_args = ["--hiero", "--player", "--studio", "--nukeassist"]
    if set(nuke.rawArgs) & set(invalid_args):
        raise ImportError("pyblish-nuke only works in Nuke or NukeX.")

except ImportError as e:
    nuke.tprint("pyblish: Could not load integration: %s " % e)

else:

    import pyblish_nuke

    # Setup integration
    pyblish_nuke.setup()
