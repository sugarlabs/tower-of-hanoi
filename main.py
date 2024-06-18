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

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import pygame
from gamestatemanager import GameStateManager
from level import Level

from gettext import gettext as _

FPS = 30
GAME_SIZE = 640, 360

class TowerOfHanoi:
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption(_("Tower Of Hanoi"))
        self.screen = pygame.display.set_mode(GAME_SIZE, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager("level 1")
        self.states = {}
        for i in range(1, 8):
            self.states["level " + str(i)] = Level(i, self)

    def run(self):
        self.is_running = True
        while self.is_running:
            curr_state = self.states[self.gameStateManager.get_state()]
            while Gtk.events_pending():
                Gtk.main_iteration()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                curr_state.handle_event(event)

            curr_state.run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    g = TowerOfHanoi()
    g.run()
