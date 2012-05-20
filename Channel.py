#!/usr/bin/python

from time import time
from telepathy.server import ChannelTypeText

class caveTextChannel(ChannelTypeText):
    def Send(self, message_type, text):
        # tell the chat client, "yeah, i sent that"
        self.Sent(int(time()), message_type, text)
        # now tell the chat client we got a reply :-)
        self.Received(0, int(time()), self._handle.get_id(),\
            message_type, 0, text)

# make sure the channel shuts down properly
    def Close(self):
        self.remove_from_connection()
        self.Closed()

