import gi 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#
# Child of Gtk.Window - One argument "text you want to display" 
# Builds ui 
#
class MyWindow(Gtk.Window):
      def __init__(self, myText):
          Gtk.Window.__init__(self, title="Dude!")
          self.ui(myText)
      
      def ui(self, myText):
          self.set_border_width(24)
          text = Gtk.Label(myText)
          self.add(text) 

