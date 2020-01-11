import os
import pygame
import random

width, height = 500, 600
screen = pygame.display.set_mode((width, height))
running = True
FPS = 60

numb_of_clouds = 8
live = True
change_of_height = 0
all_speeds = [random.randrange(2, 5) for i in range(numb_of_clouds)]
koords = [[0, 0], [125, 50], [60, 120], [430, 500], [300, 300], [530, 500], [100, 500], [250, 470]]

clock = pygame.time.Clock()


class Cloud:
    def __init__(self):
        self.width, self.height = 500, 600

    def show(self):
        for koor in koords:
            screen.blit(cloud, tuple(koor))
            if koor[1] <= self.height:
                a = koor[1] + all_speeds[koords.index(koor)]
                koor[1] = a
            else:
                koor[1] = -30


class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 20))
        self.image.fill(pygame.Color('brown'))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 4)
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 5)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            self.rect.x += self.speedx
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
            self.rect.x += self.speedx
        if keystate[pygame.K_UP]:
            self.speedy = -8
            self.rect.y += self.speedy
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
            self.rect.y += self.speedy
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0


def load_image(name, colorkey=None):
    fullname = os.path.join('pictures', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


cloud = pygame.transform.scale(load_image('cloud.png', -1), (100, 30))
player = Player()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
all_sprites.add(player)
for i in range(4):
    p = Platforms()
    all_sprites.add(p)
    mobs.add(p)

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    screen.fill((pygame.Color('blue')))
    Cloud().show()
    all_sprites.draw(screen)
    pygame.display.flip()