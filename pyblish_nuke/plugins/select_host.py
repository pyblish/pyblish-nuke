import pyblish.api


@pyblish.api.log
class SelectHostVersion(pyblish.api.Selector):
    """Inject the hosts version into context
    """

    hosts = ['nuke']
    version = (0, 1, 0)

    def process(self, context):
        context.set_data('host', value='nuke')
