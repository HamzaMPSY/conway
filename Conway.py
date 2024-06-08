import itertools
import sys
from copy import deepcopy

import pygame
from loguru import logger

# Consts
RED   = pygame.Color(255,0,0)
GREEN = pygame.Color(0,255,0)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
GRAY = pygame.Color(128,128,128)


class Conway(object):
    def __init__(self,height,width,nbr_rows, nbr_cols) -> None:
        check_errors = pygame.init()
        if check_errors[1] > 0:
            logger.error('(!) had {0} initializing errors, exiting...'.format(check_errors[1]))
            logger.error(pygame.get_error())
            sys.exit(-1)
        else :
            logger.info('(+) PyGame successfully initialized!')
        
        self.height = height
        self.width = width
        self.nbr_rows = nbr_rows
        self.nbr_cols = nbr_cols

        self.front_grid = [[False for _ in range(self.nbr_rows)] for _ in range(self.nbr_cols)]
        self.back_grid = [[False for _ in range(self.nbr_rows)] for _ in range(self.nbr_cols)]
        self.play_surface = pygame.display.set_mode((self.height,self.width))
        self.fps_controller = pygame.time.Clock()
        self.running = False
        self.tile_width = self.width // self.nbr_cols
        self.tile_height = self.height // self.nbr_rows
        self.border_right = self.tile_width/10
        self.border_bottom = self.tile_height/10
        pygame.display.set_caption('Conway Game Of Life!')
    
    def draw_panel(self):
        font = pygame.font.Font(None, 64)
        text = font.render("Game Status", True, (10, 10, 10))
        textpos = text.get_rect(x=10, y=10)
        self.play_surface.blit(text, textpos)
        
        
    def draw_grid(self):
        for row in range(self.nbr_rows):
            for col in range(self.nbr_cols):
                tile = pygame.Rect(row*self.tile_width + self.tile_width/10 ,col*self.tile_height + self.tile_width/10 ,self.tile_width - self.border_right,self.tile_height - self.border_bottom)
                color = BLACK if self.front_grid[row][col] else WHITE
                pygame.draw.rect(self.play_surface,color,tile)

    def render(self):
        self.play_surface.fill(GRAY)
        self.draw_grid()
        # self.draw_panel()
        pygame.display.flip()
        self.fps_controller.tick(30)
    
    def read_action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Exit button clicked!")
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3):
                pos = pygame.mouse.get_pos()
                self.front_grid[pos[0]//self.tile_height][pos[1]//self.tile_width] = not self.front_grid[pos[0]//self.tile_height][pos[1]//self.tile_width]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.running = not self.running

    def count_nbors(self,row,col):
        nbors = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx == 0 and dy == 0 :
                    continue;
                nbors += 1 if self.front_grid[(row + dx)%self.nbr_rows][(col + dy)%self.nbr_rows] else 0
        return nbors
    

    def step(self):
        for row in range(self.nbr_rows):
            for col in range(self.nbr_cols):
                nbors = self.count_nbors(row,col)
                self.back_grid[row][col] = (nbors == 2 or nbors == 3) if self.front_grid[row][col] else nbors == 3;
                
        self.front_grid = deepcopy(self.back_grid)

    def run(self):
        while True:
            self.render()
            self.read_action()
            if self.running:
                self.step()
            
