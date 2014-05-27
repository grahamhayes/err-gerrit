# This is a skeleton for Err plugins, use this to get started quickly.

from errbot import BotPlugin, botcmd
from pygerrit.client import GerritClient
import logging


class Gerrit(BotPlugin):
    """An Err plugin skeleton"""
    min_err_version = '1.6.0'  # Optional, but recommended
    max_err_version = '2.0.0'  # Optional, but recommended

    def activate(self):
        """Triggers on plugin activation

        You should delete it if you're not using it to
        override any default behaviour"""

        self.client = GerritClient("gerritssh")
        self.client.gerrit_version()
        self.client.start_event_stream()
        self.start_poller(2, self._poll_event)
        super(Gerrit, self).activate()

    def deactivate(self):
        """Triggers on plugin deactivation

        You should delete it if you're not using it to
        override any default behaviour"""
        logging.warn('Calling Stop Poller')
        self.stop_poller(self._poll_event)
        logging.warn('Calling Stop event stream')
        self.client.stop_event_stream()
        logging.warn('Calling super deavtivate')
        super(Gerrit, self).deactivate()

    def _poll_event(self):
        logging.warn('Starting to listen for event')
        event = self.client.get_event(block=True, timeout=1)
        if event:
            self.send('#mugsie-test', 'Got an Event', message_type='groupchat')
        logging.warn('Stopped listening for event')

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def example(self, mess, args):
        """A command which simply returns 'Example'"""
        return "Example"
