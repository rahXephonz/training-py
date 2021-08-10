import pygame
import os
import math
from random import randint
from pygame.locals import *

clock = pygame.time.Clock()
FPS_RATE = 60

#assets
player = pygame.image.load((r'C:/Users/Quetzalcoatl/Documents/Tutorial Python/Latihan OOP/Project Game/Space Invader/asset1/player1.png'))



#membuat kelas game dan atributnya
class Game():

    def tampilan_game(self):
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Zombie Attacker")
        #self.screen.blit(castle, (0, 30))
        return self.screen

    def key_input(self):
        if keys["top"]:
            playerpos[1] -= 5 # kurangi nilai y
        elif keys["bottom"]:
            playerpos[1] += 5 # tambah nilai y 
        if keys["left"]:
            playerpos[0] -= 5 # kurangi nilai x
        elif keys["right"]:
            playerpos[0] += 5 # tambah nilai x
        
#inisialisasi pygame
pygame.init()
width, height = 640, 480

#key input
keys = {
    "top": False,
    "bottom": False,
    "left": False,
    "right": False,
}

running = True
playerpos = [160, 210]
enemy_timer = 100
enemies = [[width, 100]]


#peluru
score = 0
arrows = []
 

while running:

    #fungsi pemanggilan
    game = Game()
    screen = game.tampilan_game()

    #fungsi key
    game.key_input()

    #fungsi pemindahan user dan peluru
    mouse_position = pygame.mouse.get_pos()
    angle = math.atan2(mouse_position[1] - (playerpos[1]+20), mouse_position[0] - (playerpos[0]+20))
    player_rotation = pygame.transform.rotate(player, 0 - angle * 50)
    new_playerpos = (playerpos[0] - player_rotation.get_rect().width / 2, playerpos[1] - player_rotation.get_rect().height / 2)
    screen.blit(player_rotation, new_playerpos)


    #update display
    pygame.display.flip() 

    #event looping
    for event in pygame.event.get():
        # event saat tombol exit diklik
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
           arrows.append([angle, new_playerpos[0]+59, new_playerpos[1]+59])
           shoot_sound.play()

        # cek the keydown and keyup
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys["top"] = True
            elif event.key == K_a:
                keys["left"] = True
            elif event.key == K_s:
                keys["bottom"] = True
            elif event.key == K_d:
                keys["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys["top"] = False
            elif event.key == K_a:
                keys["left"] = False
            elif event.key == K_s:
                keys["bottom"] = False
            elif event.key == K_d:
                keys["right"] = False
                
    clock.tick(FPS_RATE)
    # - End of event loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




