#!/usr/bin/env python
#
#       window.py
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
import terminal
import menu
from subprocess import Popen, PIPE

# the main window
class DesktopBase(gtk.Window):
    terminals = []
    selected_tab = 0

    def __init__(self):
        gtk.Window.__init__(self)  
        self.connect('destroy', lambda w: gtk.main_quit())
        self.set_default_size(640,480)  
        self._notebook = gtk.Notebook()
        self._vbox = gtk.VBox()
        self.add(self._vbox)
        self._vbox.pack_start(self._notebook, True)  
        
        self._notebook.connect('switch-page', self.on_notebook_page_switched)
        self._notebook.set_show_border(False)
                
        self._menu = menu.ContextMenu(self)
        self.add_accel_group(self._menu.accel_group)
        self.on_new_tab_clicked(None)

        self.maximize()
        self.set_decorated(False)      
        self.set_keep_below(True)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        
        self.show_all()
    
    def set_tabs_visible(self):
        self.show_all()

    def on_new_tab_clicked(self,widget):
        term = terminal.DesktopTerminal()
        term.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        term.connect('button-press-event', self.on_terminal_clicked)
        self.terminals.append(term)
        self._notebook.append_page(self.terminals[len(self.terminals)-1], gtk.Label("Terminal " + str(len(self.terminals))))
        self.set_tabs_visible()
    
    def on_close_tab_clicked(self,widget):
        if len(self.terminals) > 1:
            self._notebook.remove_page(self.selected_tab)
            self.terminals.remove(self.terminals[self.selected_tab])
            print "Removed, terminal count: " + str(len(self.terminals))
        self.set_tabs_visible()

    def on_next_tab_clicked(self,widget):
        if len(self.terminals) > 1 and self.selected_tab != (len(self.terminals) - 1):
            print "Moving to next tab"
            self._notebook.set_current_page(self.selected_tab + 1)
    
    def on_previous_tab_clicked(self,widget):
        if len(self.terminals) > 1 and self.selected_tab != 0:
            print "Moving to previous tab"
            self._notebook.set_current_page(self.selected_tab - 1)
    
    def on_terminal_clicked(self, widget, event):
        if event.button == 3:
            print "Terminal count: " + str(len(self.terminals))
            if len(self.terminals) > 1:
                self._menu._menuCloseTab.set_sensitive(True)
            else:
                self._menu._menuCloseTab.set_sensitive(False)
            if self.selected_tab == (len(self.terminals) - 1):
                self._menu._menuNextTab.set_sensitive(False)
            else:
                self._menu._menuNextTab.set_sensitive(True)
            if self.selected_tab == 0:
                self._menu._menuPreviousTab.set_sensitive(False)
            else:
                self._menu._menuPreviousTab.set_sensitive(True)
            self.set_tabs_visible()
            self._menu.show_all()
            self._menu.popup(None,None,None,event.button, event.time)

    def on_notebook_page_switched(self, widget, page, page_num):
        self.selected_tab = page_num
        print "Selected page is " + str(self.selected_tab)
        self.set_tabs_visible()
        
    def on_new_terminal_clicked(self,widget):
        print "New Terminal Opened"
        # this should be read from config file to determine: xterm, 
        # xfce4-terminal, gnome-terminal, etc....
        proc = Popen('xterm', shell=True, stdout=PIPE, stderr=PIPE)
        #out = str.join(proc.stdout.readlines())
        #outerr = str.join(proc.stderr.readlines())

    def on_quit_clicked(self,widget):
        sys.exit(0)
