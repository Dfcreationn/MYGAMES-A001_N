from Variabels import Window as win
from Variabels import Input as inp
from Variabels import Colours as col
from Variabels import MovingSignals as msi


import pygame
import sys

window = pygame.display.set_mode((1000, 700))


def windowcreation():
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    msi.up = 1

                else:
                    msi.up = 0

                if event.key == pygame.K_DOWN:
                    msi.down = 1

                else:
                    msi.down = 0

                if event.key == pygame.K_LEFT:
                    msi.left = 1

                else:
                    msi.left = 0

                if event.key == pygame.K_RIGHT:
                    msi.right = 1

                else:
                    msi.right = 0

        if msi.up == 1:
            msi.player_y = +msi.speed
            print(msi.player_y)
            msi.up = 0
            window.fill(col.white)

        if msi.down == 1:
            msi.player_y = -msi.speed
            print(msi.player_y)
            msi.down = 0
            window.fill(col.red)

        if msi.left == 1:
            msi.player_x = +msi.speed
            print(msi.player_x)
            msi.left = 0
            window.fill(col.blue)

        if msi.right == 1:
            msi.player_x = -msi.speed
            print(msi.player_x)
            msi.right = 0

        pygame.display.update()


def tpt():
    windowcreation()


tpt()
