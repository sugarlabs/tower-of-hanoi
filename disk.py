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

class Disk():
    def __init__(self, color, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color

    def moveAt(self, mid, bottom):
        self.mid = mid
        self.bottom = bottom
    
    def draw(self, screen):
        sw = screen.get_width()
        sh = screen.get_height()
        rectangle = pygame.Rect(0, 0, self.width / 800 * sw, self.height / 400 * sh)
        rectangle.midbottom = (self.mid / 800 * sw, self.bottom / 400 * sh)
        pygame.draw.rect(screen, self.color, rectangle, 0, 5)
    
    def putInFocus(self):
        self.bottom = 90