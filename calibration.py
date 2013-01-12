#! /usr/bin/env python
##
##  Monitor Calibration Pattern
##  Copyright (C) 2013 Ingo Ruhnke <grumbel@gmail.com>
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygtk
import math
from datetime import datetime, timedelta
pygtk.require('2.0')
import gtk, gobject, cairo

def draw_grid(img):
    cr = cairo.Context(img)
    cr.set_antialias(False)
    cr.set_source_rgb(1,1,1)
    cr.translate(0.5, 0.5)
    cr.set_line_width(1)
    for y in range(0, img.get_height(), 2):
        cr.move_to(0,y)
        cr.line_to(img.get_width()+0.5, y)
        cr.stroke()

def main(args):
    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, 256, 256)

    cr = cairo.Context(img)
    cr.set_source_rgb(0,0,0)
    cr.paint()

    draw_grid(img)

    img.write_to_png("/tmp/out.png")

if __name__ == "__main__":
    main([])

# EOF #
