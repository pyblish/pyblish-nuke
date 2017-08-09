import pyblish.api


class SelectHostVersion(pyblish.api.ContextPlugin):
    """Inject the hosts version into context"""

    order = pyblish.api.CollectorOrder
    hosts = ["nuke"]

    def process(self, context):
        import nuke
        context.data["hostVersion"] = nuke.NUKE_VERSION_STRING
