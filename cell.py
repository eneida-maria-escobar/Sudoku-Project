import pygame
from constants import *
from sudoku_generator import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row+1
        self.col = col+1
        self.selected = False
        self.screen = screen
        self.width = WIDTH // 9  # Cell width 100
        self.height = HEIGHT // 9  # Cell height 100

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        number = str(self.value)
        number_font = pygame.font.Font(None, 50)
        number_surface = number_font.render(number, 0, LINE_COLOR)
        number_rectangle = number_surface.get_rect(center=((self.col * 80 - 40, self.row * 80 - 40)))
        if self.value != 0:
            self.screen.blit(number_surface, number_rectangle)

    def get_cell_value(self):
        return self.value
