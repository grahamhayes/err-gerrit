# This is a skeleton for Err plugins, use this to get started quickly.

from errbot import BotPlugin, botcmd
from pygerrit.client import GerritClient
import time


class Gerrit(BotPlugin):
    """An Err plugin skeleton"""
    min_err_version = '1.6.0'  # Optional, but recommended
    max_err_version = '2.0.0'  # Optional, but recommended

    def activate(self):
        """Triggers on plugin activation

        You should delete it if you're not using it to
        override any default behaviour"""
        super(Gerrit, self).activate()
        self.client = GerritClient("gerritssh")
        self.client.start_event_stream()

    def deactivate(self):
        """Triggers on plugin deactivation

        You should delete it if you're not using it to
        override any default behaviour"""
        super(Gerrit, self).deactivate()
        self.client.stop_event_stream()

    def callback_connect(self):
        """Triggers when bot is connected

        You should delete it if you're not using it to
        override any default behaviour"""

        while True:
            event = self.client.get_event()
            if event:
                yield ("Event: %s", event)
            else:
                time.sleep(2)

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def example(self, mess, args):
        """A command which simply returns 'Example'"""
        return "Example"
