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

class PauseMenu:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.bg = pygame.image.load('./assets/main-menu-background.png')
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))

        self.scroll = pygame.image.load('./assets/scroll.png')
        self.scroll = pygame.transform.scale_by(self.scroll, 6)
        self.scroll_rect = self.scroll.get_rect(midtop = (self.screen.get_width()/2, 25))

        self.logo = pygame.image.load('./assets/logo.png')
        self.logo_rect = self.logo.get_rect(center = (230, 160))

        self.buttons = pygame.sprite.Group()
        self.resume_button = Button("Resume", 440, 120, self.gameStateManager, None)
        self.restart_button = Button("Restart", 440, 170, self.gameStateManager, None)
        self.home_button = Button("Home", 440, 220, self.gameStateManager, "main-menu")

        self.buttons.add([self.resume_button, self.restart_button, self.home_button])

    def set_target(self, target):
        self.restart_button.targetState = target
        self.resume_button.targetState = target        
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.check_press() and button == self.restart_button:
                        self.game.states[self.gameStateManager.get_state()].reset_level()

    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.scroll, self.scroll_rect)
        self.screen.blit(self.logo, self.logo_rect)
        self.buttons.draw(self.screen)

    def run(self):
        self.buttons.update()
        self.render()
