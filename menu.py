#!/usr/bin/env python
#
#       menu.py
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

class ContextMenu(gtk.Menu):
    window_visible = True
    def __init__(self, window):
        gtk.Menu.__init__(self)
        self._window = window
        #self._tray = traywidget
        
        self.accel_group = gtk.AccelGroup()
        
        self._menuItemNewTerminal = gtk.ImageMenuItem(gtk.STOCK_OPEN, self.accel_group)
        self.append(self._menuItemNewTerminal)
        self._menuItemNewTerminal.get_children()[0].set_label('Open Terminal')
        self._menuItemNewTerminal.connect('activate', self._window.on_new_terminal_clicked)

        self._menuSep1 = gtk.MenuItem()
        self.append(self._menuSep1)
        
        self._menuItemNewTab = gtk.ImageMenuItem(gtk.STOCK_NEW, self.accel_group)
        self.append(self._menuItemNewTab)
        self._menuItemNewTab.get_children()[0].set_label('New Tab')
        self._menuItemNewTab.connect('activate', self._window.on_new_tab_clicked)
        
        self._menuCloseTab = gtk.ImageMenuItem(gtk.STOCK_CLOSE, self.accel_group)
        self.append(self._menuCloseTab)
        self._menuCloseTab.get_children()[0].set_label('Close Tab')
        self._menuCloseTab.connect('activate', self._window.on_close_tab_clicked)
        
        #self._menuSep2 = gtk.MenuItem()
        #self.append(self._menuSep2)
        
        self._menuNextTab = gtk.ImageMenuItem(gtk.STOCK_GO_FORWARD, self.accel_group)
        self.append(self._menuNextTab)
        self._menuNextTab.get_children()[0].set_label('Next Tab')
        self._menuNextTab.connect('activate', self._window.on_next_tab_clicked)

        self._menuPreviousTab = gtk.ImageMenuItem(gtk.STOCK_GO_BACK, self.accel_group)
        self.append(self._menuPreviousTab)
        self._menuPreviousTab.get_children()[0].set_label('Previous Tab')
        self._menuPreviousTab.connect('activate', self._window.on_previous_tab_clicked)

        self._menuSep3 = gtk.MenuItem()
        self.append(self._menuSep3)

        self._menuCopy = gtk.ImageMenuItem(gtk.STOCK_COPY, self.accel_group)
        self.append(self._menuCopy)
        #self._menuCopy.connect('activate', self.on_copy_clicked)

        self._menuPaste = gtk.ImageMenuItem(gtk.STOCK_PASTE, self.accel_group)
        self.append(self._menuPaste)
        #self._menuPaste.connect('activate', self.on_paste_clicked)
        
        self._menuSep4 = gtk.MenuItem()
        self.append(self._menuSep4)

        self._menuShowHide = gtk.MenuItem("Show/Hide")
        self.append(self._menuShowHide)
        self._menuShowHide.connect('activate', self.on_show_hide_clicked)
        
        self._menuSep5 = gtk.MenuItem()
        self.append(self._menuSep5)

        self._menuItemQuit = gtk.ImageMenuItem(gtk.STOCK_QUIT, self.accel_group)
        self.append(self._menuItemQuit)
        self._menuItemQuit.connect('activate', self._window.on_quit_clicked)

        self.show_all()
        
    def on_show_hide_clicked(self,widget):
        self.toggle_window()

    # toggle whether the window is visible or not
    def toggle_window(self):
        print "Toggling window"
        if self.window_visible == True:
            self.window_visible = False
            self._window.hide()
        else:
            self.window_visible = True
            self._window.show()
        self._window.set_keep_below(True)
