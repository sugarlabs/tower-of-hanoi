#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Tower Of Hanoi
# Copyright (C) 2024 Vaibhav Sangwan
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
#
# Contact information:
# Vaibhav Sangwan    sangwanvaibhav02@gmail.com

import pygame

GAME_SIZE = 640, 360

class Utils:
    scaled_screen_rect = None

    def norm_cursor_pos():
        rect = Utils.scaled_screen_rect
        mx, my = pygame.mouse.get_pos()
        dx = mx - rect.left
        dy = my - rect.top
        mouse_norm_x = dx * GAME_SIZE[0] / rect.width
        mouse_norm_y = dy * GAME_SIZE[1] / rect.height

        return mouse_norm_x, mouse_norm_y
