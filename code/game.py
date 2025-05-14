#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
from code.Const import MENU_OPTION
#from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            #score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                pass

            elif menu_return == MENU_OPTION[3]:
                pass
                #score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()

