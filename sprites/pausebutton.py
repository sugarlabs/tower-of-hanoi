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


class PauseButton(pygame.sprite.Sprite):
    def __init__(self, x, y, gameStateManager, targetState, game):
        super().__init__()
        self.gameStateManager = gameStateManager
        self.targetState = targetState
        self.game = game

        self.image = pygame.image.load('./assets/pause-button.png')
        self.rect = self.image.get_rect(center=(x, y))

    def check_press(self):
        if self.rect.collidepoint(Utils.norm_cursor_pos()):
            curr_state = self.game.states[self.targetState]
            curr_state.set_target(self.gameStateManager.get_state())
            self.gameStateManager.set_state(self.targetState)
            return True
        return False

    def update(self):
        pass
