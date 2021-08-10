import pygame

# variable global adalah variabel yang bisa diakses di kelas atau dimanapun
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Cross the road"
SCREEN_ICON = pygame.image.load('asset/icon.png')

# fps clock = variabel global
clock = pygame.time.Clock()

# gamma color variable global
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

#inisialisasi font dan bgm
pygame.font.init()
pygame.mixer.init()

#bgm
pygame.mixer.music.load('asset/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.30)

#font
font = pygame.font.SysFont('Impact', 75)


class Game:
    
    # variabel khusus dalam screen game mengatur fpss
    FPS_RATE = 60

    # self menunjukan function ini terdaftar dalam atribut class game
    # __init__ adalah constructor didalam class game

    def __init__(self, image_path, title, icon, width, height):

        self.title = title
        self.icon = icon
        self.width = width
        self.height = height

        # self.game_screen bagian dari class game
        self.game_screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        pygame.display.set_icon(icon)
        self.game_screen.fill(WHITE_COLOR) #tidak diganti karena tidak ada back ground di constructor

        background_image = pygame.image.load(image_path)
        self.background = pygame.transform.scale(background_image, (width, height))

    # self akan muncul atau adalah bagian dari kelas game
    def run_game_loop(self, level_speed):

        is_game_over = False
        did_win = False
        direction = 0

        #inisialisasi objek
        player_character = PlayerCharacter('asset/pemain.png', 330, 600, 50, 50)
        onepiece = GameObject('asset/onepiece.png', 330, 50, 50, 50)
        #ENEMY
        enemy0 = EnemyCharacter('asset/musuh1.png', 20, 500, 50, 50)
        enemy0.SPEED *= level_speed

        enemy1 = EnemyCharacter('asset/musuh2.png', self.width - 40, 300, 50, 50)
        enemy1.SPEED *= level_speed

        enemy2 = EnemyCharacter('asset/musuh3.png', 20, 150, 50, 50)
        enemy2.SPEED *= level_speed

        #looping
        while not is_game_over:

            for event in pygame.event.get():
                # event saat tombol exit diklik
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        direction = 1
                    elif event.key == pygame.K_s:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        direction = 0

            #inisialisasi player dan enemy dan menampilkan screen

            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.background, (0, 0))
            onepiece.draw(self.game_screen)
            player_character.move(direction, self.height)
            #menggambar ke tampilan game = self.game_screen
            player_character.draw(self.game_screen)

            enemy0.move(self.width)
            enemy0.draw(self.game_screen)

            if level_speed > 2:
                enemy1.move(self.width)
                enemy1.draw(self.game_screen)
            if level_speed > 3:
                enemy2.move(self.width)
                enemy2.draw(self.game_screen)

            if player_character.detection_colission(enemy1):
                did_win = False
                text = font.render('YOU LOSE! :(', True, BLACK_COLOR)
                self.game_screen.blit(text, (200, 320))
                pygame.display.update()
                clock.tick(1)
                break

            elif player_character.detection_colission(onepiece):
                did_win = True
                text = font.render('YOU WIN! :D', True, BLACK_COLOR)
                self.game_screen.blit(text, (180, 320))
                pygame.display.update()
                clock.tick(1)
                break

            #update_screen
            pygame.display.update()
            #fps
            clock.tick(self.FPS_RATE)#menambahkan self karena termasuk ke dalam class game

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return

# superclass
class GameObject:
    # inisialisasi
    def __init__(self, image_path, x, y, width, height):

        #atribut
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

        # membuat inisalisasi gambar
        object_player = pygame.image.load(image_path)
        # scale
        self.player = pygame.transform.scale(object_player, (width, height))


    # menggambar karakter dan posisi karakter
    def draw(self, player):
        player.blit(self.player, (self.x_pos, self.y_pos))

# sub class nya memiliki atribut yang sama
class PlayerCharacter(GameObject):

    SPEED = 7

    def __init__(self, image_path, x, y, width, height):
        # super = mewariskan atau bisa memanggil kembali dari kelas lainnya
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            # gerakan ke atas
            self.y_pos -= self.SPEED

        elif direction < 0:
            # gerakan turun
            self.y_pos += self.SPEED
                        #lebih besar
        if self.y_pos >= max_height - 100:
            self.y_pos = max_height - 100

    def detection_colission(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True


class EnemyCharacter(GameObject):

    SPEED = 7

    def __init__(self, image_path, x, y, width, height):
        # super = mewariskan atau bisa memanggil kembali dari kelas lainnya
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):

        #jika enemy ingin bergerak kekiri
        if self.x_pos <= 40:
            self.SPEED = abs(self.SPEED)

        #jika enemy ingin bergerak ke kanan - 20 nilai awal kekiri
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED




# inisialisasi fungsi pygame dan class
pygame.init()
# memanggil semua atribut didalam kelas game karena constructor dan diinisialisasi dgn variable global
# urutan harus sama dengan constructor
# urutan argumen1,argumen2,argumen3,argumen4
new_game = Game('asset/background.png', SCREEN_TITLE, SCREEN_ICON, SCREEN_WIDTH, SCREEN_HEIGHT)
# memanggil method run_game_loop di class Game
new_game.run_game_loop(1)

# end of programWWW
pygame.quit()
quit()





