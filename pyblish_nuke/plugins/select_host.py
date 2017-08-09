import pyblish.api


class SelectHostVersion(pyblish.api.ContextPlugin):
    """Inject the host into context"""

    order = pyblish.api.CollectorOrder
    hosts = ["nuke"]

    def process(self, context):
        import pyblish.api

        context.data["host"] = pyblish.api.current_host()
