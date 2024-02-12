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

class Win_message():
    def __init__(self):
        self.image = pygame.image.load('./assets/win.png').convert_alpha()
        self.rect = self.image.get_rect(center = (400, 200))
    
    def draw(self, screen):
        sw = screen.get_width()
        sh = screen.get_height()
        image = pygame.transform.scale(self.image, (self.image.get_width()/800 * sw, self.image.get_height()/400 * sh))
        rect = image.get_rect(center = (sw/2, sh/2))
        screen.blit(image, rect)