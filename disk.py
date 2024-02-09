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
        self.rectangle = pygame.Rect(0, 0, width, height)
    
    def update(self):
        pass

    def moveAt(self, mid, bottom):
        self.rectangle.midbottom = (mid, bottom)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle, 0, 5)
    
    def putInFocus(self):
        self.rectangle.bottom = 100