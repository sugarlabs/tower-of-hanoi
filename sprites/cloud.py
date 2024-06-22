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
import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self, x = 750, y = 50):
        super().__init__()
        self.image = pygame.image.load("./assets/clouds/" + str(random.randint(0, 2)) +".png")
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()