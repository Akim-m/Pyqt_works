from gi.repository import Gtk

class ourwindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title= "Demonstration")
        Gtk.Window.set_default_size(self,400,325)
        Gtk,Window.set_position(self,Gtk.WindowPosition.CENTER)
        