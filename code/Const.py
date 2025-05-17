import pygame

# C
C_BLUE = (70,130,180)
C_YELLOW = (238, 173, 45)
C_GOLD = (255,215,0)
C_WHITE = (255, 255, 255)
C_ORANGE = (255, 128, 0)
C_GREEN  = (60,179,113)
C_CYAN = (0, 128, 128)
C_RED = (139,0,0)
C_LIME = (152,251,152)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
EVENT_POINT = pygame.USEREVENT + 3
EVENT_DIAMOND = pygame.USEREVENT + 4
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 3,
    'Enemy1': 2,
    'Enemy2': 1,
    'Point': 1,
    'Point1': 1
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 5,
    'Enemy1': 50,
    'Enemy2': 60,
    'Point': 1,
    'Point1': 1

}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': 1,
    'Enemy1': 1,
    'Enemy2': 2,
    'Point': 1,
    'Point1': 1
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Player1': 0,
    'Enemy1': 1,
    'Enemy2': 1,
    'Point': 8,
    'Point1': 12
}

# G
GOVER_OPTION =  {"New Game": (50, 240),
                "Return to Menu": (380, 240)
                 }

# K
KNOCKBACK_DISTANCE = 100

# M
MENU_OPTION = ('START GAME',
               'SCORE',
               'EXIT')


# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}


# S
SPAWN_TIME = 2000
SPAWN_POINT = 1500
SPAWN_DIAMOND = 8000


# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 60000  # 60s

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

