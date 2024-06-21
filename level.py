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
from background import Background
from rod import Rod
from cursor import Cursor
from disk import Disk
from cloud import Cloud
from win_message import Win_message

# USER_EVENT for spawning clouds
SPAWNCLOUD = pygame.USEREVENT + 1

DISK_COLORS = [
    "#76428a",
    "#639bff",
    "#99e550",
    "#6abe30",
    "#fbf236",
    "#e58c4f",
    "#e55757",
]
DISK_HEIGHT = 15
DISK_RADII = [150, 130, 110, 90, 70, 50, 30]

font_m = pygame.font.Font("./fonts/3Dventure.ttf", 24)

class Level:
    def __init__(self, level, game):
        self.level = level
        self.screen = game.screen
        self.gameStateManager = game.gameStateManager
        self.game = game

        self.source = Rod(120, 305)
        self.aux = Rod(320, 305)
        self.target = Rod(520, 305)
        self.rods = [self.source, self.aux, self.target]

        self.background = Background("level")
        self.has_won = False

        self.clouds = pygame.sprite.Group()
        self.clouds.add(Cloud())
        pygame.time.set_timer(SPAWNCLOUD, 12000)
        self.reset_level()

    def reset_level(self):
        self.moves = 0
        self.rodIndex = 0

        self.disks = []
        for i in range(7 - self.level, 7):
            self.disks.append(Disk(DISK_COLORS[i], DISK_RADII[i], DISK_HEIGHT))
            self.source.putOnTop(self.disks[-1])
        self.diskInFocus = None
        
        self.cursor = Cursor()
    
    def render(self):
        self.background.draw(self.screen)

        self.clouds.update()
        self.clouds.draw(self.screen)

        for disk in self.disks:
            disk.draw(self.screen)
        
        self.cursor.draw(self.screen)

        score_text = font_m.render(f'{self.moves}', False, "black")
        score_text_rect = score_text.get_rect(center = (320, 25))
        self.screen.blit(score_text, score_text_rect)

        if self.has_won:
            self.win_message.draw(self.screen)
    
    def handle_event(self, event):
        if event.type == SPAWNCLOUD:
            self.clouds.add(Cloud())
        elif event.type == pygame.KEYDOWN and not self.has_won:
            if event.key == pygame.K_LEFT:
                self.rodIndex = ((self.rodIndex - 1) + 3) % 3
                self.cursor.moveToRod(self.rods[self.rodIndex])
                if self.diskInFocus:
                    self.diskInFocus.mid = self.rods[self.rodIndex].mid
            elif event.key == pygame.K_RIGHT:
                self.rodIndex = (self.rodIndex + 1) % 3
                self.cursor.moveToRod(self.rods[self.rodIndex])
                if self.diskInFocus:
                    self.diskInFocus.mid = self.rods[self.rodIndex].mid

            elif event.key == pygame.K_UP:
                curr_disk = self.rods[self.rodIndex]
                if not self.diskInFocus:
                    self.diskInFocus = curr_disk.pullFromTop()
            elif event.key == pygame.K_DOWN:
                if self.diskInFocus and self.rods[self.rodIndex].putOnTop(
                    self.diskInFocus
                ):
                    self.diskInFocus = None
                    self.moves += 1

            elif event.key == pygame.K_r:
                self.reset_level()

        elif event.type == pygame.KEYDOWN and self.has_won:
            if event.key == pygame.K_SPACE:
                if self.level < 7:
                    self.gameStateManager.set_state("level " + str(self.level + 1))
                else:
                    self.gameStateManager.set_state("main-menu")

        
    def run(self):
        if len(self.target.disks) == self.level or len(self.aux.disks) == self.level:
            self.has_won = True
            self.win_message = Win_message(self.level, self.moves)
        
        self.render()
