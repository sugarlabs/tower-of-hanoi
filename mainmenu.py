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

from button import Button

class MainMenu:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button("PLAY", 320, 180, self.gameStateManager, "level 1"))
        self.buttons.add(Button("HELP", 320, 230, self.gameStateManager, "help"))

        self.bg = pygame.image.load('./assets/main-menu-background.png')
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))

        self.logo = pygame.image.load('./assets/logo.png')
        self.logo_rect = self.logo.get_rect(center = (320, 90))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                button.check_press()
    
    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.logo, self.logo_rect)
        self.buttons.draw(self.screen)

    def run(self):
        self.buttons.update()
        self.render()
