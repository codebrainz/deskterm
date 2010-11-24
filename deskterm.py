#!/usr/bin/env python
#
#       deskterm.py
#       
#       Copyright 2009 Matthew Brush <mbrush@ubuntu-laptop>
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

import tray
import terminal
import window
import menu

if __name__ == '__main__':
    win = window.DesktopBase()
    tray = tray.TrayWidget(win)
    menu = menu.ContextMenu(win)
    win.add_accel_group(menu.accel_group)
    win.show_all()
    gtk.main()
