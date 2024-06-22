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

from sprites.button import Button

class LevelSelectMenu:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.bg = pygame.image.load('./assets/main-menu-background.png')
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))

        self.buttons = pygame.sprite.Group()

        button_pos = (
            (120, 80),
            (320, 80),
            (520, 80),
            (120, 160),
            (320, 160),
            (520, 160),
            (320, 240)
        )
        
        for i in range(len(button_pos)):
            self.buttons.add(Button(
                "Level " + str(i + 1),
                button_pos[i][0],
                button_pos[i][1],
                self.gameStateManager,
                "level " + str(i + 1)
            ))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.check_press():
                    self.game.states[button.targetState].reset_level()
        
    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.buttons.draw(self.screen)

    def run(self):
        self.buttons.update()
        self.render()
