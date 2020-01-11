import pygame
import os
import sys
from Background import Background
from Platforms import Platforms, Land
from Wings import Wings
from Doodle import Doodle

pygame.init()
size = width, height = 500, 600
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

clock = pygame.time.Clock()


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


# высший результат всех игр
record_height = 'record'
# главный герой
doodle = pygame.transform.scale(load_image('doodle.png', -1), (510, 340))
# прыгающий doodle
doodle_jump = pygame.transform.scale(load_image('doodle_jump.png', -1), (510, 340))
# крылья
wings = pygame.transform.scale(load_image('wings.png', -1), (18, 12))
# doodle с крыльями
doodle_wings = pygame.transform.scale(load_image('doodle_wings.png', -1), (90, 60))
# монстры
monster = pygame.transform.scale(load_image('monster.png', -1), (90, 60))
# картинка облака
cloud = pygame.transform.scale(load_image('cloud.png'), (90, 60))
# платформа из земли
platf1 = pygame.transform.scale(load_image('platf1.png', -1), (90, 60))
# платформа из земли поменьше
platf2 = pygame.transform.scale(load_image('platf2.png', -1), (90, 60))
# платформа из дерева
platf_tr = pygame.transform.scale(load_image('platf_tr.png', -1), (90, 60))
# сломанная платформа из дерева
platf_br = pygame.transform.scale(load_image('platf_br.png', -1), (90, 60))
earth = load_image('land.png', -1)  # земля

doodle_size = dood_widt, dood_heigh = 90, 60
main = Doodle()
back = Background()
plate = Platforms()
land = Land()
platforms = [land]
monsters = []
land_height = 540

FPS = 60
v = 3
jump_time = 0
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
    global doodle
    intro_text = ["Нажимая клавиши 'вправо', 'влево',",
                  "перемещайте героя на платформы.",
                  "Избегайте монстров и старайтесь не падать.",
                  "Крылья помогут вам взлететь!"]

    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, record_height), 'r+') as f:
        record = int(f.read())
    fon = pygame.transform.scale(load_image('fon.jpg'), size)

    run = True
    time_picture = 0
    start = False
    while run:
        ev = None
        for event in pygame.event.get():
            ev = None
            if event.type == pygame.QUIT:
                run = False
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if start is False:
                    doodle = pygame.transform.scale(load_image('doodle.png', -1), (90, 60))
                    start = True
                ev = event
        if start:
            the_game(time_picture, ev)  # начинаем игру
        else:
            if int(time_picture % 2) == 0:
                start_pictures(fon, intro_text, record)
                screen.blit(doodle, (-20, 170))
            else:
                start_pictures(fon, intro_text, record)
                screen.blit(doodle_jump, (-20, 170))
        time_picture += v / FPS
        pygame.display.flip()
        clock.tick(FPS)


def drawing():
    global platforms
    if platforms[0].get_pos()[1] > 0:
        screen.blit(earth, land.get_pos())
    for i in platforms[1:]:
        screen.blit(platf1, land.get_pos())


def collis(main_pos):
    global platforms, dood_widt, dood_heigh
    main_x, main_y = main_pos
    touch = False
    for i in platforms:
        if main_x + dood_widt >= i.get_pos()[0] and\
                (main_y + dood_heigh <= i.get_pos()[1] or main_y <= i.get_pos()[1] + i.get_heigh()) or\
                (main_x <= i.get_pos()[0] + i.get_width()) and\
                (main_y + dood_heigh >= i.get_pos()[1] or main_y >= i.get_pos()[1] + i.get_heigh()):
            touch = True
    # (x1 + l1) >= x2 and (y1 + h1 <= y2 or y1 <= y2 + h2) or (x1 <= x2 + l2) and (y1 + h1 >= y2 or y1 >= y2 + h2)
    print(touch)
    return touch


def the_game(time, ev=None):
    global doodle, doodle_jump, jump
    if main.check_end is False:
        jump = 0
        the_end(time, back.get_result())
    else:
        screen.fill((0, 191, 255))
        screen.blit(doodle, main.get_posit())
        if ev:
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    main.left()
                elif ev.key == pygame.K_RIGHT:
                    main.right()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] < main.get_posit()[0] + 45:
                    main.left()
                elif pygame.mouse.get_pos()[0] > main.get_posit()[0] + 45:
                    main.right()
    if main.flying:
        if jump >= 20:
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
    drawing()
    if main.get_posit()[1] > 600:
        doodle = pygame.transform.scale(load_image('doodle.png', -1), (510, 340))
        the_end(time, back.get_result())


def the_end(picture_time, results):
    fon = pygame.transform.scale(load_image('fon.jpg'), size)
    start_pictures(fon, results, -5, 40)
    if int(picture_time % 2) == 0:
        screen.blit(doodle, (-20, 170))
    else:
        screen.blit(doodle_jump, (-20, 170))


start_screen()
