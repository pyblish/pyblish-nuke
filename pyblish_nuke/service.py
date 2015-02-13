# Dependencies
import pyblish_endpoint.service
from .version import version

import nuke


class NukeService(pyblish_endpoint.service.EndpointService):
    def init(self, *args, **kwargs):
        return nuke.executeInMainThreadWithResult(
            super(NukeService, self).init, args, kwargs)

    def next(self, *args, **kwargs):
        return nuke.executeInMainThreadWithResult(
            super(NukeService, self).next, args, kwargs)

    def versions(self):
        versions = super(NukeService, self).versions()
        versions["pyblish-nuke"] = version
        return versions
