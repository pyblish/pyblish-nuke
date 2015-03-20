# Dependencies
import pyblish_endpoint.service
from .version import version

import nuke

wrapper = nuke.executeInMainThreadWithResult


class NukeService(pyblish_endpoint.service.EndpointService):
    def init(self, *args, **kwargs):
        orig = super(NukeService, self).init
        return wrapper(orig, args, kwargs)

    def process(self, *args, **kwargs):
        orig = super(NukeService, self).process
        return wrapper(orig, args, kwargs)

    def versions(self):
        versions = super(NukeService, self).versions()
        versions["pyblish-nuke"] = version
        return versions
