import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

            self.rect.x = 50
            self.rect.y = 50

        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

            self.rect.x = 50
            self.rect.y = 50


class Room(object):
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):

    def __init__(self):
        super().__init__()
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [20, 90, 100, 20, BLUE],
                 [120, 90, 20, 400, BLUE],
                 [20, 230, 100, 20, BLUE],
                 [70, 470, 50, 20, BLUE],
                 [20, 420, 80, 20, BLUE],
                 [40, 340, 150, 20, BLUE],
                 [80, 380, 20, 40, BLUE],
                 [40, 340, 20, 60, BLUE],
                 [120, 150, 60, 20, BLUE],
                 [230, 20, 20, 150, BLUE],
                 [230, 220, 20, 250, BLUE],
                 [190, 260, 40, 20, BLUE],
                 [230, 410, 250, 20, BLUE],
                 [280, 470, 20, 110, BLUE],
                 [230, 220, 370, 20, BLUE],
                 [230, 170, 250, 20, BLUE],
                 [480, 100, 20, 90, BLUE],
                 [480, 100, 70, 20, BLUE],
                 [550, 50, 20, 70, BLUE],
                 [310, 50, 240, 20, BLUE],
                 [310, 50, 20, 70, BLUE],
                 [310, 120, 100, 20, BLUE],
                 [600, 150, 20, 90, BLUE],
                 [600, 150, 140, 20, BLUE],
                 [740, 150, 20, 60, BLUE],
                 [680, 190, 60, 20, BLUE],
                 [700, 230, 80, 20, BLUE],
                 [700, 230, 20, 180, BLUE],
                 [300, 290, 400, 20, BLUE],
                 [630, 370, 20, 160, BLUE],
                 [630, 510, 150, 20, BLUE],
                 [480, 350, 20, 170, BLUE],
                 [380, 350, 100, 20, BLUE],
                 [300, 300, 20, 80, BLUE]
                 ]


        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [20, 350, 270, 20, RED],
                 [120, 100, 20, 250, RED],
                 [120, 100, 600, 20, RED],
                 [200, 170, 580, 20, RED],
                 [200, 170, 20, 130, RED],
                 [290, 250, 20, 120, RED],
                 [290, 250, 300, 20, RED],
                 [700, 170, 20, 370, RED],
                 [100, 400, 600, 20, RED],
                 [20, 460, 600, 20, RED],
                 [100, 520, 600, 20, RED],
                 [360, 320, 20, 100, RED],
                 [430, 270, 20, 100, RED],
                 [500, 320, 20, 100, RED],
                 [570, 270, 20, 100, RED]
                 ]




        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [20, 350, 130, 20, GREEN],
                 [130, 100, 20, 250, GREEN],
                 [260, 20, 20, 150, GREEN],
                 [210, 150, 50, 20, GREEN],
                 [210, 150, 20, 220, GREEN],
                 [210, 350, 150, 20, GREEN],
                 [340, 350, 20, 150, GREEN],
                 [270, 480, 70, 20, GREEN],
                 [250, 430, 20, 70, GREEN],
                 [90, 430, 160, 20, GREEN],
                 [90, 430, 20, 110, GREEN],
                 [160, 480, 20, 100, GREEN],
                 [300, 250, 120, 20, GREEN],
                 [420, 250, 20, 330, GREEN],
                 [360, 90, 20, 160, GREEN],
                 [440, 20, 20, 170, GREEN],
                 [440, 170, 220, 20, GREEN],
                 [660, 90, 20, 100, GREEN],
                 [550, 90, 110, 20, GREEN],
                 [550, 230, 230, 20, GREEN],
                 [550, 230, 20, 280, GREEN],
                 [550, 500, 200, 20, GREEN],
                 [610, 450, 170, 20, GREEN],
                 [550, 400, 170, 20, GREEN],
                 [630, 350, 150, 20, GREEN],
                 [630, 300, 20, 50, GREEN],
                 [690, 250, 20, 70, GREEN],
                 [690, 300, 70, 20, GREEN]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)



def main():
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('Maze')
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    font = pygame.font.Font(None, 36)

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)


        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        screen.fill(BLACK)

        text = font.render("Don't touch the wall !!!", True, RED)
        screen.blit(text, [250, 20])

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()