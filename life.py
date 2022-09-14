# Импорты
import time

import pygame as p
import random
from pygame.locals import *

# Константы цветов RGB
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
# Создаем окно
root = p.display.set_mode((500 , 500))
p.display.set_caption('Conway`s Game of Life')
# 2х мерный список с помощью генераторных выражений
cells = [[False for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]
running = False

# Функция определения кол-ва соседей
def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count

# Основной цикл
while True:
    # Заполняем экран белым цветом
    root.fill(WHITE)
    # Выход по нажатию крестика
    for i in p.event.get():
        if i.type == QUIT:
            raise SystemExit(0)
    # Проходимся по всем клеткам
    for i in range(0, len(cells)):
        for j in range(0, len(cells[i])):
            p.draw.rect(root, (255 * cells[i][j] % 256 , 0 , 0) , [i * 20 , j * 20 , 20 , 20])
    # Обновляем экран
    p.display.update()
    cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
    events = p.event.get()
    if p.MOUSEBUTTONDOWN in [e.type for e in events]: # определяем клик
        pos = tuple([x // 20 for x in p.mouse.get_pos()])
        cells[pos[0]][pos[1]] = not cells[pos[0]][pos[1]] # меняем цвет клетки
    for e in events:
        if e.type == KEYDOWN:
            if e.key == K_RETURN: # определяем нажатие Enter
                running = not running # запускаем или остонавливаем игру
    if not running:
        continue
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]:
                if near([i, j]) not in (2 , 3):
                    cells2[i][j] = 0
                    continue
                cells2[i][j] = 1
                continue
            if near([i, j]) == 3:
                cells2[i][j] = 1
                continue
            cells2[i][j] = 0
    cells = cells2
