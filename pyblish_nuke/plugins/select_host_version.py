import pyblish.api


class CollectNukeHostVersion(pyblish.api.ContextPlugin):
    """Inject the hosts version into context"""

    label = "Nuke Version"
    hosts = ['nuke']
    order = pyblish.api.CollectorOrder - 0.5

    def process(self, context):
        import nuke
        context.data['hostVersion'] = nuke.NUKE_VERSION_STRING
