import random
import pygame

size = width, height = 500, 600
# высший результат всех игр
record_height = 'record'
doodle_size = dood_widt, dood_heigh = 90, 60
FPS = 60
v = 3
jump_time = 0
jump = 0
land_height = 540
numb_of_clouds = 8
live = True
change_of_height = 0
all_speeds = [random.randrange(2, 5) for i in range(numb_of_clouds)]
cloud_koords = [[0, 0], [125, 50], [60, 120], [430, 500], [300, 300], [530, 500], [100, 500], [250, 470]]
clock = pygame.time.Clock()
