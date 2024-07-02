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
from utils import Utils

text_font = pygame.font.Font("./fonts/3Dventure.ttf", 16)


class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y, gameStateManager, targetState):
        super().__init__()
        self.gameStateManager = gameStateManager
        self.targetState = targetState
        self.active = False
        self.text = text
        self.image = pygame.image.load('./assets/button-bg.png')
        self.text_surface = text_font.render(self.text, False, "black")
        self.text_rect = self.text_surface.get_rect(
            center=(
                self.image.get_width() / 2,
                self.image.get_height() / 2
            )
        )
        self.image.blit(self.text_surface, self.text_rect)
        self.rect = self.image.get_rect(center=(x, y))

    def check_press(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            self.gameStateManager.set_state(self.targetState)
            return True
        return False

    def update(self):
        curr_state = self.rect.collidepoint(Utils.norm_cursor_pos())
        if self.active != curr_state:
            self.active = curr_state
            if self.active:
                self.image = pygame.image.load('./assets/button-bg-active.png')
            else:
                self.image = pygame.image.load('./assets/button-bg.png')
            self.image.blit(self.text_surface, self.text_rect)
