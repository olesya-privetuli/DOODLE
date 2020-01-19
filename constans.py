import random
import pygame

size = width, height = 500, 600
# высший результат всех игр
record_height = 'record'
FPS = 60
v = 3
land_height = 540
numb_of_clouds = 7
live = True
change_of_height = 0
dood_h = 60
# скорость облаков
all_speeds = [random.randrange(2, 5) for i in range(numb_of_clouds)]
# координаты облаков
cloud_koords = [(0, 0), (125, 50), (60, 120), (300, 300), (410, 500), (100, 500), (250, 470)]
clock = pygame.time.Clock()
BLUE = (0, 192, 255)
# максимальная высота прыжка
max_h = 30
# максимальное изменение координат при прыжке
jump_h = -5
# ширина персонажа
dood_w = 90
# ширина ноги персонажа
foot_w = 20
# ширина платформы
platf_width = 90
# высота платформы
pl_heigh = 20
# ширина земли
land_w = 500
# высота земли
land_h = 50
# количество платформ на экране
numb_of_plate = 7
# новая высота для платформы
new_h = -100
# координата по y, на которых находятся платформы
platf_heights = [520, 410, 300, 210, 120, 30, -60]
# дополнительная высота
dop_h = 70
max_dood_h = 70
dood_shift = 10
min_dood_h = 310
text_coor = (10, 10)
