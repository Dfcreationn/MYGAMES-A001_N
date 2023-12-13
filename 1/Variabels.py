import pygame


class Window:
    window = pygame.display.set_mode((9000, 700))


class Input:
    key = pygame.key.get_pressed()


class MovingSignals:
    up = 0
    down = 0
    left = 0
    right = 0
    player_y = 0
    player_x = 0
    speed = 10


class Colours:
    black = (0, 0, 0)
    white = 255, 255, 255
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
