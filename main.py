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
from background import Background
from rod import Rod
from disk import Disk
from cursor import Cursor
from cloud import Cloud
from win_message import Win_message

from gettext import gettext as _

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

# USER_EVENT for spawning clouds
SPAWNCLOUD = pygame.USEREVENT + 1

class TowerOfHanoi:
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption(_("Tower Of Hanoi"))
        self.clock = pygame.time.Clock()
        self.disks = []
        self.level = 1
        self.moves = 0
        self.clouds = pygame.sprite.Group()
        self.clouds.add(Cloud())
        pygame.time.set_timer(SPAWNCLOUD, 12000)

    def load_level(self):
        self.screen.fill("white")
        self.background = pygame.sprite.GroupSingle()
        self.background.add(Background(self.screen, self.state))
        self.disks = []
        self.source = Rod(120, 305)
        self.aux = Rod(320, 305)
        self.target = Rod(520, 305)
        for i in range(7 - self.level, 7):
            self.disks.append(Disk(DISK_COLORS[i], DISK_RADII[i], DISK_HEIGHT))
            self.source.putOnTop(self.disks[-1])
        self.rods = [self.source, self.aux, self.target]
        self.rodIndex = 0
        self.diskInFocus = None
        self.cursor = Cursor()

    def instructions_state(self):
        for event in self.py_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "running"
                    self.background.sprite.change_state(self.state)
                    self.load_level()

    def won_state(self):
        for event in self.py_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "running"
                    self.background.sprite.change_state(self.state)
                    self.moves = 0
                    self.level += 1
                    if self.level > 7:
                        self.level = 1
                    self.load_level()
            elif event.type == SPAWNCLOUD:
                self.clouds.add(Cloud())

        self.clouds.update()
        self.clouds.draw(self.screen)
        self.cursor.draw(self.screen)

        for disk in self.disks:
            disk.draw(self.screen)

        self.win_message.draw(self.screen)

    def running_state(self):
        for event in self.py_events:
            if event.type == pygame.KEYDOWN:
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
                    self.load_level()
            elif event.type == SPAWNCLOUD:
                self.clouds.add(Cloud())

        self.clouds.update()
        self.clouds.draw(self.screen)        
        self.cursor.draw(self.screen)

        for disk in self.disks:
            disk.draw(self.screen)

        if len(self.target.disks) == self.level or len(self.aux.disks) == self.level:
            self.win_message = Win_message(self.level, self.moves)
            self.state = "won"

    # game states -> instructions (press space to move to running state),
    # running (controls and restart), won (press space to return to home
    # screen)
    def run(self):
        self.state = "instructions"

        self.screen = pygame.display.set_mode((640, 360), pygame.SCALED)
        self.screen.fill("white")
        self.background = pygame.sprite.GroupSingle()
        self.background.add(Background(self.screen, self.state))

        self.is_running = True
        while self.is_running:
            while Gtk.events_pending():
                Gtk.main_iteration()
            self.py_events = pygame.event.get()
            for event in self.py_events:
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.screen.fill("white")
            self.background.sprite.draw(self.screen)

            if self.state == "running":
                self.running_state()
            elif self.state == "instructions":
                self.instructions_state()
            elif self.state == "won":
                self.won_state()

            pygame.display.update()
            self.clock.tick(30)


if __name__ == "__main__":
    g = TowerOfHanoi()
    GAME_SIZE = (640, 360)
    g.screen = pygame.display.set_mode(GAME_SIZE, pygame.SCALED)
    g.run()
