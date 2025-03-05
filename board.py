import pygame
from constants import *
from cell import Cell
from sudoku_generator import *


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = [[0 for i in range(9)] for i in range(9)]
        self.sud_board = generate_sudoku(9, self.difficulty)
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                val = self.sud_board[i][j]
                a = Cell(val, i, j, self.screen)
                self.board[i][j] = a

    def draw(self):
        # draw lines
        # draw horizontal lines
        for i in range(1, BOARD_ROWS + 1):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * CELL_SIZE),
                (WIDTH, i * CELL_SIZE),
                LINE_WIDTH
            )

        # draw vertical lines
        for j in range(1, BOARD_COLS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (j * CELL_SIZE, 0),
                (j * CELL_SIZE, HEIGHT - HEIGHT_WIDTH_DIFFERENCE),
                LINE_WIDTH
            )

        # draw bold lines for each 3x3
        # Bold horizontal lines
        for o in range(3, 12, 3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, o * CELL_SIZE),
                (WIDTH, o * CELL_SIZE),
                BOLD_LINE_WIDTH
            )
        # Bold vertical lines
        for k in range(3, 9, 3):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (k * CELL_SIZE, 0),
                (k * CELL_SIZE, HEIGHT - HEIGHT_WIDTH_DIFFERENCE),
                BOLD_LINE_WIDTH
            )

    def select(self, row, col):
        if col <= 8 and row <= 8:
            pygame.draw.line(
                self.screen,
                SELECTED_CELL_LINE_COLOR,
                (col * 80, row * 80),
                (col * 80 + 80, row * 80),
                SELECTED_CELL_LINE_WIDTH
            )
            pygame.draw.line(
                self.screen,
                SELECTED_CELL_LINE_COLOR,
                (col * 80, row * 80),
                (col * 80, row * 80 + 80),
                SELECTED_CELL_LINE_WIDTH
            )
            pygame.draw.line(
                self.screen,
                SELECTED_CELL_LINE_COLOR,
                (col * 80 + 80, row * 80 + 80),
                (col * 80, row * 80 + 80),
                SELECTED_CELL_LINE_WIDTH
            )
            pygame.draw.line(
                self.screen,
                SELECTED_CELL_LINE_COLOR,
                (col * 80 + 80, row * 80),
                (col * 80 + 80, row * 80 + 80),
                SELECTED_CELL_LINE_WIDTH
            )

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def reset_to_original(self):
        self.board = [[0 for i in range(9)] for i in range(9)]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                val = self.sud_board[i][j]
                a = Cell(val, i, j, self.screen)
                self.board[i][j] = a

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass

    def original_board(self):
        lst = []
        for i in range(9):
            for j in range(9):
                lst.append(self.sud_board[i][j])
        return lst
