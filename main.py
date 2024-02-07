import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import pygame
from sys import exit
from background import Background
from rod import Rod
from disk import Disk
from cursor import Cursor

DISK_COLORS = ["#76428a", "#639bff", "#99e550", "#6abe30", "#fbf236", "#e58c4f", "#e55757"]
DISK_HEIGHT = 15
DISK_RADII = [150, 130, 110, 90, 70, 50, 30]
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
LEVEL = 1

class TowerOfHanoi:
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption('Tower Of Hanoi')
        self.clock = pygame.time.Clock()
        self.disks = []
    
    def load_level(self):
        self.screen.fill("white")
        self.background = pygame.sprite.GroupSingle()
        self.background.add(Background(self.screen, self.state))
        self.disks = []
        self.source = Rod(200, 341)
        self.aux = Rod(400, 341)
        self.target = Rod(600, 341)
        for i in range(7 - LEVEL, 7):
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
        global LEVEL
        for event in self.py_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "instructions"
                    self.background.sprite.change_state(self.state)
                    LEVEL += 1
                    if LEVEL > 7:
                        LEVEL = 1

        self.cursor.draw(self.screen)
        self.cursor.update()

        for disk in self.disks:
            disk.draw(self.screen)
            
        self.screen.blit(self.win_message, self.win_rect)
        


    def running_state(self):
        global LEVEL
        for event in self.py_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rodIndex = ((self.rodIndex - 1) + 3)%3
                    self.cursor.moveToRod(self.rods[self.rodIndex])
                    if self.diskInFocus:
                        self.diskInFocus.rectangle.centerx = self.rods[self.rodIndex].mid
                elif event.key == pygame.K_RIGHT:
                    self.rodIndex = (self.rodIndex + 1)%3
                    self.cursor.moveToRod(self.rods[self.rodIndex])
                    if self.diskInFocus:
                        self.diskInFocus.rectangle.centerx = self.rods[self.rodIndex].mid

                elif event.key == pygame.K_UP:
                    if not self.diskInFocus:
                        self.diskInFocus = self.rods[self.rodIndex].pullFromTop()
                elif event.key == pygame.K_DOWN:
                    if self.diskInFocus and self.rods[self.rodIndex].putOnTop(self.diskInFocus):
                        self.diskInFocus = None
                
                elif event.key == pygame.K_r:
                    self.load_level()
        
        self.cursor.draw(self.screen)
        self.cursor.update()

        for disk in self.disks:
            disk.draw(self.screen)
        
        if(len(self.target.disks) == LEVEL):
            self.state = "won"
            self.win_message = pygame.image.load('./assets/win.png').convert_alpha()
            self.win_rect = self.win_message.get_rect(center = (400, 200))
    
    # game states -> instructions (press space to move to running state), running (controls and restart), won (press space to return to home screen)
    def run(self):
        global SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL
        self.state = "instructions"

        self.screen = pygame.display.get_surface()
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
                elif event.type == pygame.VIDEORESIZE:
                    SCREEN_WIDTH = event.size[0]
                    SCREEN_HEIGHT = event.size[1]
                    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)
                    # self.background.sprite.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
            
            self.screen.fill("white")
            self.background.draw(self.screen)

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
    GAME_SIZE = (800, 400)
    g.screen = pygame.display.set_mode(GAME_SIZE, pygame.RESIZABLE)
    g.run()