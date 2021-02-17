#!/usr/bin python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#
# Create a window object and sets size.
#
win = Gtk.Window()
win.set_border_width(24)
#
# Text to be displayed.
#
text = Gtk.Label("Stretch for 15 minutes")

#
# Sets title for the window.
# Add text to the window Object.
#
win.set_title("Dude!")
win.add(text)

win.connect("destroy", Gtk.main_quit) # Sets X icon to terminate program.
win.show_all()                        # Displays the window on the screen.
Gtk.main()                            # Starts the event loop.
