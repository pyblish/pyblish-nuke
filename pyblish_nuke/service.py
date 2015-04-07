# Dependencies
import pyblish_endpoint.service

import nuke

wrapper = nuke.executeInMainThreadWithResult


class NukeService(pyblish_endpoint.service.EndpointService):
    def init(self, *args, **kwargs):
        orig = super(NukeService, self).init
        return wrapper(orig, args, kwargs)

    def process(self, *args, **kwargs):
        orig = super(NukeService, self).process
        return wrapper(orig, args, kwargs)

    def repair(self, *args, **kwargs):
        orig = super(NukeService, self).repair
        return wrapper(orig, args, kwargs)
