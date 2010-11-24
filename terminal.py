#!/usr/bin/env python
#
#       terminal.py
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
import vte

# TODO: figure out why colors won't work.
#       create methods for property adjustments

# the virtual terminal widget
class DesktopTerminal(vte.Terminal):
    def __init__(self):
        vte.Terminal.__init__(self)
        self.set_background_image_file("background.png")
        self.set_background_saturation(1.0)
        self.set_font_from_string_full("monospace 9", False)
        self.set_colors_default()
        self.fork_command()
        #self.feed_child('tput setaf 1 && clear\n')

    def set_colors_default(self):
        fg_color = gtk.gdk.color_parse('#FF0000')
        bg_color = gtk.gdk.color_parse('#FFFFFF')
        self.set_color_foreground(fg_color)
        self.set_color_background(bg_color)

