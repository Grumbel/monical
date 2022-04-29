#!/usr/bin/env python3

# calibration - Python script for generating Monitor Calibration Pattern
# Copyright (C) 2013,2015,2018 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
import pygame

from pygame import Surface, Color, Rect, draw


def draw_grid(scr: Surface, bg: Color, fg: Color, rect: Rect) -> None:
    draw.rect(scr, bg, rect)

    for x in range(rect.left, rect.right, 2):
        h = min(rect.right - x - 1, rect.height - 1)
        draw.line(scr, fg, (x, rect.top), (x + h, rect.top+h))

    for y in range(rect.top+2, rect.bottom, 2):
        w = min(rect.bottom - y - 1, rect.width - 1)
        draw.line(scr, fg, (rect.left, y), (rect.left+w, y + w))


def draw_grid_pattern(scr: Surface, bg: Color, fg: Color, rect: Rect, tw: int=32, th: int=32) -> None:
    for y in range(0, rect.height, tw):
        for x in range(0, rect.width, th):
            if (x//tw+y//th) % 2 == 0:
                draw.rect(scr, bg, Rect(x, y, tw, th))
            else:
                draw.rect(scr, fg, Rect(x, y, tw, th))


def draw_gamma_ramp(scr: Surface, bg: Color, fg: Color, rect: Rect, tw: int=16) -> None:
    for y in range(0, rect.height, 2):
        draw.line(scr, bg, (rect.left, y), (rect.right, y))
        draw.line(scr, fg, (rect.left, y+1), (rect.right, y+1))

    for y in range(0, rect.height):
        p = float(y) / (rect.height-1)
        gamma = 1.0 / (2.2 - 0.5 + p)
        draw.line(scr,
                  Color(int(255 * ((fg.r/255.0 * 0.5) ** gamma)),
                        int(255 * ((fg.g/255.0 * 0.5) ** gamma)),
                        int(255 * ((fg.b/255.0 * 0.5) ** gamma))),
                  (rect.centerx-tw, y), (rect.centerx+tw, y))


def draw_test(scr: Surface, bg: Color, fg: Color, c: Color, rect: Rect) -> None:
    draw_grid(scr, bg, fg, rect)

    draw.rect(scr, c,
              Rect(rect.left,
                   rect.centery - 16,
                   rect.width, 32))

    draw.rect(scr, c,
              Rect(rect.centerx - 16,
                   rect.top,
                   32, rect.height))


def draw_ramp(scr: Surface, color: Color, rect: Rect, steps: int) -> None:
    w = rect.width/steps
    for p in range(0, steps):
        draw.rect(scr,
                  Color(p * color.r // (steps-1),
                        p * color.g // (steps-1),
                        p * color.b // (steps-1)),
                  Rect(rect.left + p * w,
                       rect.top,
                       w, rect.height))

    draw.rect(scr,
              Color(127, 127, 127),
              rect, 1)


def draw_fs_test(scr: Surface) -> None:
    draw_test(scr,
              Color(255, 0, 0),
              Color(0, 0, 0),
              Color(186, 0, 0),
              Rect(100, 100, 400, 300))

    draw_test(scr,
              Color(0, 255, 0),
              Color(0, 0, 0),
              Color(0, 186, 0),
              Rect(600, 100, 400, 300))

    draw_test(scr,
              Color(0, 0, 255),
              Color(0, 0, 0),
              Color(0, 0, 186),
              Rect(100, 500, 400, 300))

    draw_test(scr,
              Color(255, 255, 255),
              Color(0, 0, 0),
              Color(186, 186, 186),
              Rect(600, 500, 400, 300))

    draw_ramp(scr,
              Color(255, 255, 255),
              Rect(100, 750, 800, 40),
              10)

    draw_ramp(scr,
              Color(255, 0, 0),
              Rect(100, 800, 800, 40),
              10)

    draw_ramp(scr,
              Color(0, 255, 0),
              Rect(100, 850, 800, 40),
              10)

    draw_ramp(scr,
              Color(0, 0, 255),
              Rect(100, 900, 800, 40),
              10)

# # draw background
# rect = Rect(width/2 - 32, 0, 64, height)
# color = Color(0, 0, 0)
# draw.rect(scr, color, rect)

# # draw grid
# color = Color(0, 255, 0)
# for y in range(-width, height, 2):
#     draw.line(scr, color, (0, y), (width, y+width))

# # draw box
# rect = Rect(width/2 - 16, 0, 32, height)
# color = Color(0, 186, 0)
# draw.rect(scr, color, rect)

# rect = Rect(0, height/2 - 16, width, 32)
# draw.rect(scr, color, rect)


def draw_fs_red(scr: Surface) -> None:
    draw_test(scr,
              Color(255, 0, 0),
              Color(0, 0, 0),
              Color(186, 0, 0),
              scr.get_rect())


def draw_fs_green(scr: Surface) -> None:
    draw_test(scr,
              Color(0, 255, 0),
              Color(0, 0, 0),
              Color(0, 186, 0),
              scr.get_rect())


def draw_fs_blue(scr: Surface) -> None:
    draw_test(scr,
              Color(0, 0, 255),
              Color(0, 0, 0),
              Color(0, 0, 186),
              scr.get_rect())


def draw_fs_white(scr: Surface) -> None:
    draw_test(scr,
              Color(255, 255, 255),
              Color(0, 0, 0),
              Color(186, 186, 186),
              scr.get_rect())


def draw_fs_ramp(scr: Surface) -> None:
    draw_ramp(scr,
              Color(255, 255, 255),
              Rect(100, 750, 800, 40),
              10)

    draw_ramp(scr,
              Color(255, 0, 0),
              Rect(100, 800, 800, 40),
              10)

    draw_ramp(scr,
              Color(0, 255, 0),
              Rect(100, 850, 800, 40),
              10)

    draw_ramp(scr,
              Color(0, 0, 255),
              Rect(100, 900, 800, 40),
              10)


def draw_fs_circle(scr: Surface) -> None:
    rect = scr.get_rect()
    draw_grid_pattern(scr, Color(112, 112, 112), Color(144, 144, 144), rect)
    flip = True
    for r in range(min(rect.width, rect.height)//2, 0, -32):
        if flip:
            draw.circle(scr, Color(0, 0, 0), rect.center, r)
        else:
            draw.circle(scr, Color(255, 255, 255), rect.center, r)
        flip = not flip


def draw_fs_gamma_ramp(scr: Surface) -> None:
    rect = scr.get_rect()
    scr.fill(Color(0, 0, 0))

    params = [(100, Color(0, 0, 0), Color(255, 255, 255)),
              (350, Color(0, 0, 0), Color(255, 0, 0)),
              (600, Color(0, 0, 0), Color(0, 255, 0)),
              (850, Color(0, 0, 0), Color(0, 0, 255))]

    for x, bg, fg in params:
        draw_gamma_ramp(scr,
                        bg, fg,
                        Rect(x, rect.top, 200, rect.width))


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((1280, 960), pygame.RESIZABLE)

    mode = 0
    modes = [draw_fs_test,
             draw_fs_gamma_ramp,
             draw_fs_red,
             draw_fs_green,
             draw_fs_blue,
             draw_fs_white,
             draw_fs_ramp,
             draw_fs_circle]

    while True:
        modes[mode](screen)
        pygame.display.flip()

        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mode = (mode + 1) % len(modes)
            elif event.key == pygame.K_RIGHT:
                mode = (mode - 1) % len(modes)
            elif event.key == pygame.K_ESCAPE:
                sys.exit()


if __name__ == "__main__":
    main()


# EOF #
