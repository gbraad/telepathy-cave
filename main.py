#!/usr/bin/python

# IMPORTANT! makes asynchronous dbus things work
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)

# get the mainloop before creating the ConnectionManager
# so that dbus (telepathy) can use it
from gobject import MainLoop
ml = MainLoop()

from cave import caveConnectionManager

# get telepathy to start listening for our dbus stuff via the mainloop
caveConnectionManager()
# and ... Go!
ml.run()

