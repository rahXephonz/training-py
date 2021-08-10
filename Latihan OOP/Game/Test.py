import pygame
import os
from pygame import *

width, height = 640, 480
pygame.init()

class Game():
    
    def screen(self):
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Castle Attacker")
        self.screen.blit(self.background, (0, 0))
 
    
    @property
    def icon(self):
        self.icon = pygame.image.load((r'C:/Users/Quetzalcoatl/Documents/resources/castle1.png'))
 
    @property
    def background(self):
        self.background = pygame.image.load((r'C:/Users/Quetzalcoatl/Documents/resources/city.png'))
    
    @icon.getter
    def icon(self):
        return self.icon
    @background.getter
    def background(self):
        return self.background

running = True
while running:

    #fungsi pemanggilan
    game = Game()
    game.screen()
    for event in pygame.event.get():
        # event saat tombol exit diklik
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)    
