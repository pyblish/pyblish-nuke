import pyblish.api


class SelectHostVersion(pyblish.api.ContextPlugin):
    """Inject the host into context"""

    hosts = ["nuke"]
    order = pyblish.api.CollectorOrder - 0.5
    version = (0, 1, 0)

    def process(self, context):
        context.data["host"] = pyblish.api.current_host()
