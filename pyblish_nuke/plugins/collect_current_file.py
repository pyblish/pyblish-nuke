import pyblish.api


class CollectCurrentFile(pyblish.api.ContextPlugin):
    """Inject the current working file into context"""

    label = "Current File"
    hosts = ['nuke']
    order = pyblish.api.CollectorOrder - 0.5
    version = (0, 1, 0)

    def process(self, context):
        """Todo, inject the current working file"""
        import os
        import nuke

        current_file = nuke.root().name()
        normalised = os.path.normpath(current_file)

        context.data['currentFile'] = normalised
