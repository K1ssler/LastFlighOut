import sys

import pygame
from pygame import Surface
from code.Const import  WIN_WIDTH, WIN_HEIGHT, C_ORANGE, C_RED, C_WHITE, GOVER_OPTION


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/GameOver.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.options = GOVER_OPTION
        self.option_names = list(self.options.keys())
        self.selected_index = 0
        self.sound = pygame.mixer.Sound('./asset/GameOver.wav')
        self.cursor_sound = pygame.mixer.Sound('./asset/Move.flac')

    def show(self):
        self.window.blit(self.surf, self.rect)


        self.Game_Over_text(80, "Game Over", C_RED, center=(WIN_WIDTH // 2, 100))

        # display formatted text
        x_spacing = 300
        total_width = (len(self.option_names) - 1) * x_spacing
        start_x = (WIN_WIDTH // 2) - (total_width // 2)
        y = WIN_HEIGHT - 100

        for i, name in enumerate(self.option_names):
            x = start_x + i * x_spacing
            color = C_ORANGE if i == self.selected_index else C_WHITE
            self.Game_Over_text(20, name, color, center=(x, y))

    def update_selection(self, direction: str) -> str:
        if direction == "left":
            self.cursor_sound.play()
            self.selected_index = (self.selected_index - 1) % len(self.option_names)
        elif direction == "right":
            self.cursor_sound.play()
            self.selected_index = (self.selected_index + 1) % len(self.option_names)
        return self.option_names[self.selected_index]

    def run(self) -> str:
        self.sound.play()

        clock = pygame.time.Clock()
        while True:
            self.window.fill((0, 0, 0))
            self.show()
            pygame.display.flip()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_LEFT, pygame.K_a]:
                        self.update_selection("left")
                    elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                        self.update_selection("right")
                    elif event.key == pygame.K_RETURN:
                        return self.option_names[self.selected_index]

    def Game_Over_text(self, text_size: int, text: str, text_color: tuple, center: tuple):
        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect(center=center)
        self.window.blit(surf, rect)
