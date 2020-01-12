import pygame
import os
import sys
import random
from Background import Background
from Platforms import Platforms, Land
from Doodle import Doodle
from cloud import Cloud
from constans import size, record_height, FPS, v, clock, cloud_koords, BLUE, platf_koords
from constans import max_h, platf_width, numb_of_plate

pygame.init()
screen = pygame.display.set_mode(size)


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


# главный герой
big_doodle = pygame.transform.scale(load_image('doodle.png', -1), (510, 340))
doodle = pygame.transform.scale(load_image('doodle.png', -1), (90, 60))
# прыгающий doodle
big_doodle_jump = pygame.transform.scale(load_image('doodle_jump.png', -1), (510, 340))
doodle_jump = pygame.transform.scale(load_image('doodle_jump.png', -1), (90, 60))
# крылья
wings = pygame.transform.scale(load_image('wings.png', -1), (18, 12))
# doodle с крыльями
doodle_wings = pygame.transform.scale(load_image('doodle_wings.png', -1), (90, 60))
# монстры
monster = pygame.transform.scale(load_image('monster.png', -1), (90, 60))
# картинка облака
cloud = pygame.transform.scale(load_image('cloud.png', -1), (90, 60))
# платформа из земли
platf = pygame.transform.scale(load_image('platf.png', -1), (90, 20))
# земля
earth = load_image('land.png', -1)

# длина и ширина doodle в игре
doodle_size = dood_w, dood_h = 90, 60

main = Doodle()
back = Background()
plate = Platforms()
land = Land()
platforms = [land]
for _ in range(numb_of_plate):
    platforms.append(land)
monsters = []

bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
run = True
play = True
left = False
right = False
jump = 0


def start_pictures(fon, text, record=-5, font_num=20):
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 75)
    text_coord = 50
    screen.blit(font.render('Doodle_Прыг', 1, (0, 0, 0)), (70, 10))
    font = pygame.font.Font(None, font_num)
    interval = 10
    if font_num == 40:
        interval = 20
    for line in text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += interval
        intro_rect.top = text_coord
        intro_rect.x = 30
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    if record != -5:
        screen.blit(font.render("Ваш рекорд: {}".format(record), 1, (0, 0, 0)), (10, 550))


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    global doodle, run
    intro_text = ["Нажимая клавиши 'вправо', 'влево',",
                  "перемещайте героя на платформы.",
                  "Избегайте монстров и старайтесь не падать.",
                  "Крылья помогут вам взлететь!"]

    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, record_height), 'r+') as f:
        record = int(f.read())
    fon = pygame.transform.scale(load_image('fon.jpg'), size)

    time_picture = 0
    start = False
    while run:
        if start is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    doodle = pygame.transform.scale(load_image('doodle.png', -1), (90, 60))
                    start = True
            if int(time_picture % 2) == 0:
                start_pictures(fon, intro_text, record)
                screen.blit(big_doodle, (-20, 170))
            else:
                start_pictures(fon, intro_text, record)
                screen.blit(big_doodle_jump, (-20, 170))
        else:
            playing(time_picture)
        time_picture += v / FPS
        pygame.display.flip()
        clock.tick(FPS)


def platf_drawing():
    global platforms
    if platforms[0].get_pos()[1] > 0:
        screen.blit(earth, land.get_pos())
    for _ in platforms[1:]:
        screen.blit(platf, land.get_pos())


def collis(main_pos):
    global platforms, dood_w, dood_h
    m_x, m_y = main_pos
    touch = False
    for i in platforms:
        if ((m_y + dood_h <= i.get_pos()[1] or m_y + dood_h <= i.get_pos()[1] + i.get_heigh()) or
            (m_x <= i.get_pos()[0] + platf_width)) and \
                m_x + dood_w >= i.get_pos()[0] and \
                (m_y + dood_h >= i.get_pos()[1] or m_y + dood_h >= i.get_pos()[1] + i.get_heigh()):
            touch = True
    return touch


def the_game():
    global doodle, doodle_jump, jump, cloud, left, right
    if main.check_end is False:
        jump = 0
    else:
        screen.fill(BLUE)
        for koor in cloud_koords:
            screen.blit(cloud, koor)
        screen.blit(earth, platf_koords[0])
        for pl in platf_koords[1:]:
            screen.blit(platf, pl)
        if jump == 0:
            screen.blit(doodle, main.get_posit())
        else:
            screen.blit(doodle_jump, main.get_posit())
        if left:
            main.left()
        elif right:
            main.right()
    if main.flying:
        if jump >= max_h:
            jump = 0
            main.fly()
        elif collis(main.get_posit()):
            jump = 0
        else:
            jump += 1
    elif collis(main.get_posit()):
        jump = 0
        main.fly()
    main.jump()
    if main.get_posit()[1] > 600:
        doodle = pygame.transform.scale(load_image('doodle.png', -1), (510, 340))


def the_end(picture_time, results='0'):
    fon = pygame.transform.scale(load_image('fon.jpg'), size)
    start_pictures(fon, results, -5, 40)
    if int(picture_time % 2) == 0:
        screen.blit(big_doodle, (-20, 170))
    else:
        screen.blit(big_doodle_jump, (-20, 170))


def playing(time):
    global run, play, left, right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            elif event.key == pygame.K_RIGHT:
                right = True
        elif event.type == pygame.KEYUP:
            left = False
            right = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] < main.get_posit()[0] + 45:
                main.left()
            elif pygame.mouse.get_pos()[0] > main.get_posit()[0] + 45:
                main.right()
    if play:
        Cloud().change_h()
        the_game()
    else:
        the_end(time)


start_screen()
