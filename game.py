import pygame
import os
import sys
from Result import Result
from Platforms import Plate_coor, Platforms, Land
from Doodle import Doodle
from cloud import Cloud
from Board import Board
from Monster import Monster
from constans import size, record_height, FPS, v, clock, cloud_coords, BLUE, width, text_coor
from constans import max_h, numb_of_plate, foot_w, dop_h, max_dood_h, min_dood_h, monster_height

pygame.init()
screen = pygame.display.set_mode(size)


# загрузка изображений
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
doodle = load_image('doodle.png', -1)
big_doodle = pygame.transform.scale(load_image('doodle.png', -1), (510, 340))
yellow_doodle = load_image('doodle.png', -1)
purple_doodle = load_image('purple_doodle.png', -1)
blue_doodle = load_image('doodle_blue.png', -1)
brown_doodle = load_image('doodle_brown.png', -1)
doodles = [yellow_doodle, purple_doodle, blue_doodle, brown_doodle]
# прыгающий doodle
doodle_jump = load_image('doodle.png', -1)
big_doodle_jump = pygame.transform.scale(load_image('doodle_jump.png', -1), (510, 340))
yellow_doodle_jump = load_image('doodle_jump.png', -1)
purple_doodle_jump = load_image('doodle_purple_jump.png', -1)
blue_doodle_jump = load_image('doodle_blue_jump.png', -1)
brown_doodle_jump = load_image('doodle_brown_jump.png', -1)
doodles_jump = [yellow_doodle_jump, purple_doodle_jump, blue_doodle_jump, brown_doodle_jump]
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

# главный персонаж игры
main = Doodle()
# класс ведет счет игры
result = Result()
# класс, отвечающий за платформы
plate = Platforms()
# класс, унаследованный от класса платформ, для земли
land = Land()
# класс, создающий платформы при новой игре
plate_coor = Plate_coor()
#
class_monster = Monster()
# список со всеми выводимыми платформами
platforms = [land]
for _ in range(numb_of_plate):
    platforms.append(plate)

# состояние персонажа
fall = False

# Загрузка звука прыжка
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

# вывод окна
run = True
# зажатии клавиши влево
left = False
# зажатие клавиши вправо
right = False
# изменение координаты при прыжке
jump = 0

monster_show = False


# функция отвечает за вывод картинки персонажа в начальном и конечном окне
def picture_big_doodle(time):
    if int(time % 2) == 0:
        screen.blit(big_doodle, (-20, 170))
    else:
        screen.blit(big_doodle_jump, (-20, 170))


# функция прорисовки начального окна
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


# вывод начального окна
def start_screen():
    global doodle, run
    intro_text = ["Нажимая клавиши 'вправо', 'влево',",
                  "перемещайте героя на платформы.",
                  "Избегайте монстров, ведь они обнулят ваши результаты. ",
                  "Старайтесь не падать.",
                  "Нажмите и выберите себе персонажа"]

    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, record_height), 'r+') as f:
        record = int(f.read())
    fon = pygame.transform.scale(load_image('fon.jpg'), size)

    time_picture = 0
    start = 0
    while run:
        if start == 0 or start == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    if start == 0:
                        start = 1
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        change_dood(event)
                        start = 2
            if start == 0:
                start_pictures(fon, intro_text, record)
                picture_big_doodle(time_picture)
            else:
                choice(time_picture)
        else:
            playing(time_picture)
        time_picture += v / FPS
        pygame.display.flip()
        clock.tick(FPS)


# функция для выбора персонажа
def choice(time):
    global doodles, doodles_jump
    screen.fill(BLUE)
    draw_cloud()
    for i in range(len(doodles)):
        if int(time % 2) == 0:
            draw_doodle(doodles[i], i)
        else:
            draw_doodle(doodles_jump[i], i)
    Cloud().change_h()


# прорисовка всех картинок персонажей в окне выбора персонажа
def draw_doodle(name, i):
    screen.blit(pygame.transform.scale(name, (270, 180)),
                (Board().render()[i][0], Board().render()[i][1] + dop_h))


# занесение в переменную картинки главного героя выбранного персонажа
def change_dood(event):
    global doodles, doodles_jump, doodle, doodle_jump
    num = Board().picture(event.pos)
    doodle = pygame.transform.scale(doodles[num], (90, 60))
    doodle_jump = pygame.transform.scale(doodles_jump[num], (90, 60))


# функция отвечает за касание главного героя с "монстром"
def collis_monster_with_doodle(main_pos):
    global platforms, dood_w, dood_h
    m_x, m_y = main_pos
    touch = False
    # проверка на пересечение
    if class_monster.get_all_coords()[1] < m_y + dood_h < class_monster.get_all_coords()[1] \
            + monster_height and m_x + dood_w - foot_w > class_monster.get_all_coords()[0] and \
            m_x + foot_w < class_monster.get_all_coords()[0] + monster.get_width():
        touch = True
    elif class_monster.get_all_coords()[1] < m_y < class_monster.get_all_coords()[1] \
            + monster_height and m_x + dood_w - foot_w > class_monster.get_all_coords()[0] and \
            m_x + foot_w < class_monster.get_all_coords()[0] + monster.get_width():
        touch = True
    return touch


# функция отвечает за касание главного героя с платформами
def collis_platf_with_doodle(main_pos):
    global platforms, dood_w, dood_h, land, plate
    platf_jump = plate_coor.pl_jump()
    m_x, m_y = main_pos
    touch = False
    # проверка на пересечение с платформой
    for i in range(numb_of_plate + 1):
        if i == 0:
            p = land
        else:
            p = plate
        coor = plate_coor
        if coor.get_pos(i)[1] < m_y + dood_h < coor.get_pos(i)[1] + p.get_height() and \
                m_x + dood_w - foot_w > coor.get_pos(i)[0] and \
                m_x + foot_w < coor.get_pos(i)[0] + p.get_width():
            touch = True
            if not platf_jump[i]:
                platf_jump[i] = True
                result.new_jump()
    return touch


def draw_cloud():
    for coor in cloud_coords:
        screen.blit(cloud, coor)


# сама игра
def the_game():
    global doodle, doodle_jump, jump, left, right, monster_show
    screen.fill(BLUE)
    draw_cloud()
    screen.blit(earth, plate_coor.pl_coor()[0])
    for pl in plate_coor.pl_coor()[1:]:
        screen.blit(platf, pl)
    if jump == 0:
        screen.blit(doodle, main.get_posit())
    else:
        screen.blit(doodle_jump, main.get_posit())
    if result.result_on_game() % 8 == 0:
        class_monster.update()
    elif result.result_on_game() % 8 == 1:
        monster_show = True
    if monster_show is True and class_monster.get_x() < width:
        screen.blit(monster, (class_monster.get_x(), class_monster.get_y()))
        class_monster.fly()
    else:
        monster_show = False
    font = pygame.font.Font(None, 20)
    string_rendered = font.render('Счёт: {}'.format(result.result_on_game()), 1,
                                  pygame.Color('black'))
    screen.blit(string_rendered, text_coor)
    if left:
        main.left()
    elif right:
        main.right()
    plate_coor.change_h()
    class_monster.down()
    check_h()
    if main.flying:
        if jump >= max_h:
            jump = 0
            main.fly()
        else:
            jump += 1
    elif collis_platf_with_doodle(main.get_posit()):
        jump = 0
        main.fly()
    if collis_monster_with_doodle(main.get_posit()):
        result.collis_with_monster()
    main.jump()


# перемещение платформ вниз
def check_h():
    if main.get_posit()[1] <= max_dood_h and not fall:
        class_monster.allow(True)
        plate_coor.alow(True)
        main.down()
        if main.get_fly():
            main.fly()
    elif main.get_posit()[1] >= min_dood_h:
        class_monster.allow(False)
        plate_coor.alow(False)


# вывод окна при проигрыше
def the_end(picture_time, results='0'):
    fon = pygame.transform.scale(load_image('fon.jpg'), size)
    start_pictures(fon, results, -5, 40)
    font = pygame.font.Font(None, 30)
    screen.blit(font.render('Нажмите, чтобы начать заново', 1, (0, 0, 0)), (70, 550))
    picture_big_doodle(picture_time)


# обновляет результаты при начале новой игры
def update_results():
    global main, result
    plate_coor.update()
    main = Doodle()
    result = Result()


# функция вызывается при начале игры
def playing(time):
    global run, left, right
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if main.check_end() and (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
            update_results()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            elif event.key == pygame.K_RIGHT:
                right = True
        elif event.type == pygame.KEYUP:
            left = False
            right = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] < main.get_posit()[0] + 40:
                main.left()
            elif pygame.mouse.get_pos()[0] > main.get_posit()[0] + 40:
                main.right()
    if main.check_end():
        the_end(time, result.get_result())
    else:
        Cloud().change_h()
        the_game()


start_screen()
