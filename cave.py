#!/usr/bin/python

# create a telepathy ConnectionManager for 'cave'
import dbus
from telepathy.server import ConnectionManager

from Constants import PROTOCOL, PROGRAM
from Connection import caveConnection

class caveConnectionManager(ConnectionManager):
    def __init__(self):
        ConnectionManager.__init__(self, PROGRAM)
        # use telepathy magic to provide required methods
        self._protos[PROTOCOL] = caveConnection

    def GetParameters(self, proto):
        from telepathy import NotImplemented, CONN_MGR_PARAM_FLAG_REQUIRED
        if proto != PROTOCOL:
            raise NotImplemented('unknown protocol %s' % proto)
        return [('account', CONN_MGR_PARAM_FLAG_REQUIRED, 's', '')]

