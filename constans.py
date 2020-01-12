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
all_speeds = [random.randrange(2, 5) for i in range(numb_of_clouds)]
cloud_koords = [(0, 0), (125, 50), (60, 120), (300, 300), (410, 500), (100, 500), (250, 470)]
clock = pygame.time.Clock()
BLUE = (0, 191, 255)
max_h = 30
dood_w = 90
platf_width = 90
pl_heigh = 20
numb_of_plate = 6
platf_jump = [True, False * numb_of_plate]
platf_koords = [(0, 550)]
platf_heights = [400, 320, 240, 160, 80, 0, -80]
for i in range(numb_of_plate):
    platf_koords.append((random.randint(0, width - platf_width), platf_heights[i]))
