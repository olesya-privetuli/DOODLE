import random
import pygame

size = width, height = 500, 600
# высший результат всех игр
record_height = 'record'
FPS = 60
v = 3
land_height = 540
numb_of_clouds = 8
live = True
change_of_height = 0
all_speeds = [random.randrange(2, 5) for i in range(numb_of_clouds)]
cloud_koords = [[0, 0], [125, 50], [60, 120], [430, 500], [300, 300], [530, 500], [100, 500], [250, 470]]
clock = pygame.time.Clock()
