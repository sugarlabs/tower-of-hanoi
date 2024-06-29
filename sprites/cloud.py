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
    def __init__(self, x = 640, y = 50):
        super().__init__()
        self.image = pygame.image.load("./assets/clouds/" + str(random.randint(0, 2)) +".png")
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(midright = (x, y))

    def update(self):
        if self.rect.centerx < 100 + (self.rect.width / 2):
            self.image.set_alpha(self.get_alpha_grad(self.rect.width / 2, 100 + (self.rect.width / 2)))
        elif self.rect.centerx < 540 - (self.rect.width / 2):
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(self.get_alpha_grad(640 - (self.rect.width / 2), 540 - (self.rect.width / 2)))

        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()
    
    def get_alpha_grad(self, initial, final):
        return (self.rect.centerx - initial) / (final - initial) * 255
