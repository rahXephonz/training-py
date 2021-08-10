import pygame

# variable global adalah variabel yang bisa diakses di kelas atau dimanapun
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
SCREEN_TITLE = "Zombie Attacker"
SCREEN_ICON = pygame.image.load('asset/image/icon.png')

# fps clock = variabel global
clock = pygame.time.Clock()

# gamma color variable global
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

class Game:
    
    # variabel khusus dalam screen game mengatur fpss
    FPS_RATE = 60

    # self menunjukan function ini terdaftar dalam atribut class game
    # __init__ adalah constructor didalam class game

    def __init__(self, title, icon, width, height):

        self.title = title
        self.icon = icon
        self.width = width
        self.height = height

        # screen game screen = nama variabel
        self.game_screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        pygame.display.set_icon(icon)
        self.game_screen.fill(WHITE_COLOR) #tidak diganti karena tidak ada back ground di constructor

    # self akan muncul atau adalah bagian dari kelas game
    def run_game_loop(self):

        is_game_over = False
        direction = 0

        player_character = PlayerCharacter('asset/image/infrantry.png', 160, 210, 100, 100)

        #looping
        while not is_game_over:

            for event in pygame.event.get():
                # event saat tombol exit diklik
                if event.type == pygame.QUIT:
                    is_game_over = True

            self.game_screen.fill(WHITE_COLOR)
            player_character.draw(self.game_screen)
            player_character.move(direction)

            #update_screen
            pygame.display.update()
            #fps
            clock.tick(self.FPS_RATE)#menambahkan self karena termasuk ke dalam class game
# superclass
class GameObject:
    # inisialisasi
    def __init__(self, image_path, x, y, width, height):

        #atribut
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.width = height

        # membuat inisalisasi gambar
        object_player = pygame.image.load(image_path)
        # scale
        self.player = pygame.transform.scale(object_player, (width, height))


    # menggambar karakter dan bg
    def draw(self, player):
        player.blit(self.player, (self.x_pos, self.y_pos))

# sub class nya memiliki atribut yang sama
class PlayerCharacter(GameObject):
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        # super = mewariskan atau bisa memanggil kembali dari kelas lainnya
        super().__init__(image_path, x, y, width, height)

    def move(self, direction):
        if direction > 0:
            # gerakan ke atas
            self.y_pos -= self.SPEED

        elif direction < 0:
            # gerakan turun
            self.x_pos += self.SPEED



# inisialisasi fungsi pygame dan class
pygame.init()
# memanggil semua atribut didalam kelas game karena constructor dan diinisialisasi dgn variable global
# urutan harus sama dengan constructor
# urutan argumen1,argumen2,argumen3,argumen4
new_game = Game(SCREEN_TITLE, SCREEN_ICON, SCREEN_WIDTH, SCREEN_HEIGHT)
# memanggil method run_game_loop di class Game
new_game.run_game_loop()

# end of program
pygame.quit()
quit()





