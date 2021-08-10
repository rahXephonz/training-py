import pygame

width, height = [620, 620]

pygame.init()

#asset game screen
screen_icon = pygame.image.load((r'C:/Users/Quetzalcoatl/Documents/Tutorial Python/Latihan OOP/Project Game/Space Invader/asset1/ufo.png'))
screen_background = pygame.image.load((r'C:/Users/Quetzalcoatl/Documents/Tutorial Python/Latihan OOP/Project Game/Space Invader/asset1/bg1.png'))
screen_title = "Space Invader v.2"
screen = pygame.display.set_mode((width, height))

#posisi
playerX = 270
playerY = 520
# inisialisasi game berakhir dan berhenti


#asset game
player = pygame.image.load((r'C:/Users/Quetzalcoatl/Documents/Tutorial Python/Latihan OOP/Project Game/Space Invader/asset1/player1.png'))
scale = pygame.transform.scale(player, (70, 70))

def player(x, y):
    screen.blit(scale, (x, y))


game_running = False
while not game_running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_running = True

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_a:
                print("Left arrow is pressed")
            if event.type == pygame.K_d:
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_a or event.type == pygame.K_d:
                print("key stroke has been release")

    screen.blit(screen_background, (0, 0))
    player(playerX, playerY)
    pygame.display.update()


