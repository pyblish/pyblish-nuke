import pyblish.api

import nuke


class SelectHostVersion(pyblish.api.ContextPlugin):
    """Inject the hosts version into context"""

    hosts = ['nuke']
    order = pyblish.api.CollectorOrder - 0.5
    version = (0, 1, 0)

    def process(self, context):
        context.data['hostVersion'] = nuke.NUKE_VERSION_STRING
