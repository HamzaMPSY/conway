import sys

import pygame
from loguru import logger

from Conway import Conway
from utils import get_conway_params, get_text, get_window_dimension

CONFIG_PATH = 'config.ini'


class Game:

    def __init__(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            logger.error(
                '(!) had {0} initializing errors, exiting...'.format(check_errors[1]))
            logger.error(pygame.get_error())
            sys.exit(-1)
        else:
            logger.info('(+) PyGame successfully initialized!')

        self.height, self.width = get_window_dimension(CONFIG_PATH)
        self.nbr_rows, self.nbr_cols = get_conway_params(CONFIG_PATH)
        self.menu_text = get_text(
            path=CONFIG_PATH, key='title_text', color="#b68f40")
        self.menu_rect = self.menu_text.get_rect(
            center=(self.width/2, self.height//10))

        play_button = Button(pos=(self.width/2, 4*self.height//10),
                             key="play", base_color="#d7fcd4", hovering_color="White")
        options_button = Button(pos=(self.width/2, 5*self.height//10),
                                key="options", base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(pos=(self.width/2, 6*self.height//10),
                             key="quit", base_color="#d7fcd4", hovering_color="White")

        self.menu_buttons = [play_button, options_button, quit_button]

        self.background = pygame.image.load("assets/background.png")
        self.play_surface = pygame.display.set_mode((self.width, self.height))
        self.fps_controller = pygame.time.Clock()
        pygame.display.set_caption('Conway Game Of Life: Main Menu')

    def read_action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Exit button clicked!")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3):
                pos = pygame.mouse.get_pos()
                for button in self.menu_buttons:
                    if button.check_for_input(pos):
                        if button.key == "play":
                            instance = Conway(
                                height=self.height, width=self.width, nbr_cols=self.nbr_cols, nbr_rows=self.nbr_rows)
                            instance.run()

    def render(self):
        pos = pygame.mouse.get_pos()
        for button in self.menu_buttons:
            button.change_color(pos)
        self.play_surface.blit(self.background, (0, 0))
        self.play_surface.blit(self.menu_text, self.menu_rect)
        for button in self.menu_buttons:
            button.update(self.play_surface)
        pygame.display.flip()
        self.fps_controller.tick(30)

    def run(self):
        while True:
            self.render()
            self.read_action()


class Button:
    def __init__(self, pos, key, base_color, hovering_color):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.key = key
        self.hovering_color = hovering_color
        self.base_color = base_color
        self.text = get_text(
            path=CONFIG_PATH, key=key+"_text", color=base_color)
        self.text_rect = self.text.get_rect(center=pos)

    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, pos):
        return pos[0] >= self.text_rect.left and pos[0] <= self.text_rect.right and pos[1] >= self.text_rect.top and pos[1] <= self.text_rect.bottom

    def change_color(self, pos):
        color = self.hovering_color if self.check_for_input(
            pos) else self.base_color
        self.text = get_text(
            path=CONFIG_PATH, key=self.key+"_text", color=color)
