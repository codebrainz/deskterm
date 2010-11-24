#!/usr/bin/env python
#
#       tray.py
#       
#       Copyright 2009 Matthew Brush <mbrush@leftclick.ca>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
import sys
import gtk

# this is the icon in the system tray, which controls the window passed in
class TrayWidget():
    # flag to track visible state of window, probably already exists somehwere
    # in PyGTK but I couldn't track it down
    window_visible = True
    
    # initializer, gets the main window passed to it
    def __init__(self,wnd):
        self.main_window = wnd
        self.status_icon = gtk.status_icon_new_from_file("terminal.png")
        self.status_icon.set_tooltip("DeskTerm")
        # should occur when the icon is clicked
        self.status_icon.connect('activate', self.on_statusicon_clicked)
        #self._traywidget = gtk.status_icon_new_from_file("terminal.png")
        #self._traywidget =
                # context menu
        """self._menu = gtk.Menu()

        self._menuItemClose = gtk.MenuItem("Close")
        self._menu.append(self._menuItemClose)
        self._menuItemClose.connect('activate', self.on_quit_clicked)

        self._menu.show_all()"""
        
        self.main_window.show()

    # toggle whether the window is visible or not
    def toggle_window(self):
        print "Toggling window"
        if self.window_visible == True:
            self.window_visible = False
            self.main_window.hide()
        else:
            self.window_visible = True
            self.main_window.show()
        self.main_window.set_keep_below(True)
        
    # for when the status icon is clicked
    def on_statusicon_clicked(self, widget):
        #self._menu.popup(None,None,None,3,None,1)
        self.toggle_window()
        
    def on_quit_clicked(self,widget):
        sys.exit(0)
