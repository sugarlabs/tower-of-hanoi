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
from sprites.backbutton import BackButton

font_s = pygame.font.Font("./fonts/m04b.ttf", 8)
help_text = """Tower Of Hanoi is a mathematical puzzle game. \
The goal of the game is to move the stack of disks to any one \
of the initially empty rods.

Rules
1. Only one disk can be moved at a time.
2. Larger disks cannot be put on top of smaller ones.

Controls
Up - pick up the top disk
Down - put down the picked up disk
Left - move the disk towards left
Right - move the disk towards right
"""

class HelpMenu:
    def __init__(self, game):
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.bg = pygame.image.load('./assets/main-menu-background.png')
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))

        self.backbutton = BackButton(530, 240, self.gameStateManager, "main-menu")

        self.scroll = pygame.image.load('./assets/scroll.png')
        self.scroll = pygame.transform.scale_by(self.scroll, 6)
        self.scroll_rect = self.scroll.get_rect(midtop = (self.screen.get_width()/2, 25))

        Utils.render_multiple_lines(help_text, self.scroll, 60, (60, 60), "black", font_s)
        
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.backbutton.check_press()

    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.scroll, self.scroll_rect)
        self.screen.blit(self.backbutton.image, self.backbutton.rect)

    def run(self):
        self.render()
