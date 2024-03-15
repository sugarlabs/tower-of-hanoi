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


class Background(pygame.sprite.Sprite):
    def __init__(self, screen, state):
        super().__init__()
        self.screen = screen
        self.change_state(state)
        self.rect = self.image.get_rect(topleft=(0, 0))

    def change_state(self, state):
        if state == "instructions":
            self.image = pygame.image.load(
                "./assets/instructions-background.png")
        else:
            self.image = pygame.image.load("./assets/running-background.png")

    def draw(self, screen):
        sw = screen.get_width()
        sh = screen.get_height()
        image = pygame.transform.scale(self.image, (sw, sh))
        rect = image.get_rect(topleft=(0, 0))
        screen.blit(image, rect)
