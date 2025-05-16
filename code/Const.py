import pygame

# C
C_BLUE = (70,130,180)
C_YELLOW = (238, 173, 45)
C_WHITE = (255, 255, 255)
C_ORANGE = (255, 128, 0)
C_GREEN  = (60,179,113)
#C_GREEN = (0, 128, 0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player1': 3,
    'Enemy1': 1,
    'Enemy2': 1,
}
ENTITY_SCORE = 0
ENTITY_HEALTH = 3

# M
MENU_OPTION = ('START GAME',
               'SCORE',
               'EXIT')
# O
OBSTACLE_SIZE = {
    'Obstacle': (108, 239),  # exemplo: largura 64px, altura 64px
}


# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
SPAWN_TIME = 2000

# E
