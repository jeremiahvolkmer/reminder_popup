#!/usr/local/bin python3
import gi
import my_window as mw 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk 

#
# The text displayed
#
text = "Strech for 15 minutes"

win = mw.MyWindow(text)
win.connect("destroy", Gtk.main_quit) # 'X' icon termiates program
win.show_all()
Gtk.main()
