import pygame
import math
from pygame.locals import *

width, height = 640, 480
SCREEN_TITLE = "Zombie Attacker"
SCREEN_ICON = pygame.image.load('resources/icon.png')


# inisialisasi fungsi pygame
pygame.init()
pygame.mixer.init()

# fps
clock = pygame.time.Clock()
FPS_RATE = 60

# function looping
keys = {
    "top": False,
    "bottom": False,
    "left": False,
    "right": False,
}

is_game_over = False

score = 0
arrows = []

# gamma color
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# screen
game_screen = pygame.display.set_mode((width,height))
game_screen.fill(BLACK_COLOR)
pygame.display.set_caption(SCREEN_TITLE)
pygame.display.set_icon(SCREEN_ICON)

#asset player and background
player = pygame.image.load('resources/infrantry.png')
background = pygame.image.load('resources/city.png')
tank = pygame.image.load('resources/tank.png')
arrow = pygame.image.load('resources/images/pelor.png')

# scalling tank and player
player = pygame.transform.scale(player, (100, 100))
# tank = pygame.transform.scale(tank, (130, 130))

playerpos = [120, 120]

# bgm and sfx
pygame.mixer.music.load('resources/audio/moonlight.wav')
shoot_sound = pygame.mixer.Sound('resources/audio/shoot.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.50)


class Game:

    def __init__(self,width,height,icon):
        self.width = width
        self.height = height
        self.icon = icon

    
    def background(self):
        pass

#looping
while not is_game_over:

    #draw background
    game_screen.blit(background, (0, 0))

    #draw player
    #fungsi pemindahan user dan peluru
    mouse_position = pygame.mouse.get_pos()
    angle = math.atan2(mouse_position[1] - (playerpos[1]+59), mouse_position[0] - (playerpos[0]+59))
    player_rotation = pygame.transform.rotate(player, 360 - angle * 30)
    new_playerpos = (playerpos[0] - player_rotation.get_rect().width / 2, playerpos[1] - player_rotation.get_rect().height / 2)
    game_screen.blit(player_rotation, new_playerpos)

    # 6.1 - Draw arrows
    for bullet in arrows:
        arrow_index = 0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely

        if bullet[1] < -64 or bullet[1] > width or bullet[2] < -64 or bullet[2] > height:
            arrows.pop(arrow_index)
        arrow_index += 1
        # draw the arrow
        for projectile in arrows:
            new_arrow = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            game_screen.blit(new_arrow, (projectile[1], projectile[2]))
    
    for event in pygame.event.get():
        # event saat tombol exit diklik
        if event.type == pygame.QUIT:
            is_game_over = True

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
        
    if keys["top"]:
        playerpos[1] -= 5 # kurangi nilai y
    elif keys["bottom"]:
        playerpos[1] += 5 # tambah nilai y 
    if keys["left"]:
        playerpos[0] -= 5 # kurangi nilai x
    elif keys["right"]:
        playerpos[0] += 5 # tambah nilai x  

    #update_screen
    pygame.display.update()

    #fps
    clock.tick(FPS_RATE)