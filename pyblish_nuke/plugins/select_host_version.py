import os

import pyblish.api

import nuke


@pyblish.api.log
class SelectHostVersion(pyblish.api.Selector):
    """Inject the hosts version into context
    """

    hosts = ['nuke']
    version = (0, 1, 0)

    def process_context(self, context):
        context.set_data('hostVersion', value=nuke.NUKE_VERSION_STRING)
