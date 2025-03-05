import sys

import pygame

from board import *
from cell import *
from constants import *

difficulty = None


def draw_game_start(screen):
    # Initialize font
    start_title_font = pygame.font.Font(None, 100)
    title_2_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Initialize and draw title # 2
    title_surface_2 = title_2_font.render("Select Game Mode", 0, LINE_COLOR)
    title_rectangle_2 = title_surface_2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(title_surface_2, title_rectangle_2)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 250, HEIGHT - 150))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT - 150))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 250, HEIGHT - 150))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        global difficulty
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                    return
                elif medium_rectangle.collidepoint(event.pos):
                    difficulty = 40
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = 50
                    return
        pygame.display.update()


def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)
    if winner is True:
        text = 'Game Won!'
        game_win_surf = game_over_font.render(text, 0, LINE_COLOR)
        game_win_rect = game_win_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_win_surf, game_win_rect)
    else:
        text = "Game Over :("
        game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
        game_over_rect = game_over_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_over_surf, game_over_rect)

        # # Printing reset, restart, and exit buttons
        # button_font = pygame.font.Font(None, 70)
        # # Initialize buttons
        # # Initialize text first
        # restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        # # Initialize button background color and text
        # restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        # restart_surface.fill(LINE_COLOR)
        # restart_surface.blit(restart_text, (10, 10))
        # # Initialize button rectangle
        # restart_rectangle = restart_surface.get_rect(
        #     center=(WIDTH // 2, HEIGHT - 200))
        # # Draw buttons
        # screen.blit(restart_surface, restart_rectangle)


def check_full(screen):
    for i in range(9):
        for j in range(9):
            if Sudoku_board.board[i][j].get_cell_value() == 0:
                return False
    return True


def check_col(screen):
    for i in range(9):
        lst = []
        for j in range(9):
            if Sudoku_board.board[i][j].get_cell_value() in lst:
                return False
            else:
                lst.append(Sudoku_board.board[i][j].get_cell_value())
    return True


def check_row(screen):
    for i in range(9):
        lst = []
        for j in range(9):
            if Sudoku_board.board[j][i].get_cell_value() in lst:
                return False
            else:
                lst.append(Sudoku_board.board[j][i].get_cell_value())
    return True


def check_boxes(screen):
    for i in range(0, 9, 3):  # row
        for j in range(0, 9, 3):  # col
            lst = []
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if Sudoku_board.board[x][y].get_cell_value() not in lst:
                        lst.append(Sudoku_board.board[x][y].get_cell_value())
                    else:
                        return False
    return True


def draw_selected_cell(row, col, line_color, line_width):
    pygame.draw.line(
        screen,
        line_color,
        (col * 80, row * 80),
        (col * 80 + 80, row * 80),
        line_width
    )
    pygame.draw.line(
        screen,
        line_color,
        (col * 80, row * 80),
        (col * 80, row * 80 + 80),
        line_width
    )
    pygame.draw.line(
        screen,
        line_color,
        (col * 80 + 80, row * 80 + 80),
        (col * 80, row * 80 + 80),
        line_width
    )
    pygame.draw.line(
        screen,
        line_color,
        (col * 80 + 80, row * 80),
        (col * 80 + 80, row * 80 + 80),
        line_width
    )


if __name__ == "__main__":
    Program = True
    while Program:
        pygame.quit()
        game_over = False
        winner = False
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")

        draw_game_start(screen)  # Calls function to draw start screen

        screen.fill(BG_COLOR)  # Creates a white screen
        Sudoku_board = Board(WIDTH, HEIGHT, screen, difficulty)  # Creates instance of Board
        Sudoku_board.draw()  # Draws the board (grids)
        for i in range(9):  # Put values onto board
            for j in range(9):
                Sudoku_board.board[i][j].draw()

        # Printing reset, restart, and exit buttons
        button_font = pygame.font.Font(None, 70)
        # Initialize buttons
        # Initialize text first
        reset_text = button_font.render("RESET", 0, (255, 255, 255))
        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
        exit_text = button_font.render("EXIT", 0, (255, 255, 255))
        # Initialize button background color and text
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surface.fill(LINE_COLOR)
        reset_surface.blit(reset_text, (10, 10))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(LINE_COLOR)
        restart_surface.blit(restart_text, (10, 10))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(LINE_COLOR)
        exit_surface.blit(exit_text, (10, 10))
        # Initialize button rectangle
        reset_rectangle = reset_surface.get_rect(
            center=(WIDTH // 2 - 250, HEIGHT - 100))
        restart_rectangle = restart_surface.get_rect(
            center=(WIDTH // 2, HEIGHT - 100))
        exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2 + 250, HEIGHT - 100))
        # Draw buttons
        screen.blit(reset_surface, reset_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

        Game = True
        clicked_row = 0
        clicked_col = 0
        g = True
        while Game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_rectangle.collidepoint(event.pos):
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # The Restart button will take the user back to the Game Start screen.
                    if restart_rectangle.collidepoint(event.pos):
                        Game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # The reset button will clear the board
                    if reset_rectangle.collidepoint(event.pos):
                        Sudoku_board.reset_to_original()  # resets board
                        screen.fill(BG_COLOR)  # Creates a white screen
                        Sudoku_board.draw()  # Draws the board (grids)
                        for i in range(9):  # Put values onto board
                            for j in range(9):
                                Sudoku_board.board[i][j].draw()
                        # Printing reset, restart, and exit buttons
                        button_font = pygame.font.Font(None, 70)
                        # Initialize buttons
                        # Initialize text first
                        reset_text = button_font.render("RESET", 0, (255, 255, 255))
                        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
                        exit_text = button_font.render("EXIT", 0, (255, 255, 255))
                        # Initialize button background color and text
                        reset_surface = pygame.Surface(
                            (reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
                        reset_surface.fill(LINE_COLOR)
                        reset_surface.blit(reset_text, (10, 10))
                        restart_surface = pygame.Surface(
                            (restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
                        restart_surface.fill(LINE_COLOR)
                        restart_surface.blit(restart_text, (10, 10))
                        exit_surface = pygame.Surface(
                            (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
                        exit_surface.fill(LINE_COLOR)
                        exit_surface.blit(exit_text, (10, 10))
                        # Initialize button rectangle
                        reset_rectangle = reset_surface.get_rect(
                            center=(WIDTH // 2 - 250, HEIGHT - 100))
                        restart_rectangle = restart_surface.get_rect(
                            center=(WIDTH // 2, HEIGHT - 100))
                        exit_rectangle = exit_surface.get_rect(
                            center=(WIDTH // 2 + 250, HEIGHT - 100))
                        # Draw buttons
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)

                if event.type == pygame.MOUSEBUTTONDOWN:  # Draws red box
                    if g is True:
                        if clicked_col <= 8 and clicked_row <= 8:
                            draw_selected_cell(clicked_row, clicked_col, WHITE_LINE_COLOR, SELECTED_CELL_LINE_WIDTH)
                            Sudoku_board.draw()  # Draws the board (grids)
                        clicked_row = int(event.pos[1] / CELL_SIZE)
                        clicked_col = int(event.pos[0] / CELL_SIZE)
                        if clicked_col <= 8 and clicked_row <= 8:
                            draw_selected_cell(clicked_row, clicked_col, SELECTED_CELL_LINE_COLOR, SELECTED_CELL_LINE_WIDTH)
                    elif g is False:
                        pass

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if 0 <= clicked_col and 0 < clicked_row:
                            draw_selected_cell(clicked_row, clicked_col, WHITE_LINE_COLOR, SELECTED_CELL_LINE_WIDTH)
                            Sudoku_board.draw()  # Draws the board (grids)
                            clicked_row -= 1
                            draw_selected_cell(clicked_row, clicked_col, SELECTED_CELL_LINE_COLOR,
                                               SELECTED_CELL_LINE_WIDTH)
                    if event.key == pygame.K_DOWN:
                        if clicked_col <= 8 and clicked_row < 8:
                            draw_selected_cell(clicked_row, clicked_col, WHITE_LINE_COLOR, SELECTED_CELL_LINE_WIDTH)
                            Sudoku_board.draw()  # Draws the board (grids)
                            clicked_row += 1
                            draw_selected_cell(clicked_row, clicked_col, SELECTED_CELL_LINE_COLOR,
                                               SELECTED_CELL_LINE_WIDTH)
                    if event.key == pygame.K_LEFT:
                        if clicked_col > 0 and clicked_row >= 0:
                            draw_selected_cell(clicked_row, clicked_col, WHITE_LINE_COLOR, SELECTED_CELL_LINE_WIDTH)
                            Sudoku_board.draw()  # Draws the board (grids)
                            clicked_col -= 1
                            draw_selected_cell(clicked_row, clicked_col, SELECTED_CELL_LINE_COLOR,
                                               SELECTED_CELL_LINE_WIDTH)
                    if event.key == pygame.K_RIGHT:
                        if clicked_col < 8 and clicked_row <= 8:
                            draw_selected_cell(clicked_row, clicked_col, WHITE_LINE_COLOR, SELECTED_CELL_LINE_WIDTH)
                            Sudoku_board.draw()  # Draws the board (grids)
                            clicked_col += 1
                            draw_selected_cell(clicked_row, clicked_col, SELECTED_CELL_LINE_COLOR,
                                               SELECTED_CELL_LINE_WIDTH)
                    if event.key == pygame.K_1:
                        if Sudoku_board.board[clicked_row][clicked_col].get_cell_value() == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(1, clicked_row, clicked_col, screen)
                    if event.key == pygame.K_2:
                        if Sudoku_board.board[clicked_row][clicked_col].get_cell_value() == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(2, clicked_row, clicked_col, screen)
                    if event.key == pygame.K_3:
                        if Sudoku_board.board[clicked_row][clicked_col].get_cell_value() == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(3, clicked_row, clicked_col, screen)
                    if event.key == pygame.K_4:
                        if Sudoku_board.board[clicked_row][clicked_col].get_cell_value() == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(4, clicked_row, clicked_col, screen)
                    if event.key == pygame.K_5:
                        if Sudoku_board.board[clicked_row][clicked_col].get_cell_value() == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(5, clicked_row, clicked_col, screen)
                    if event.key == pygame.K_6:
                        if Sudoku_board.board[clicked_row][clicked_col].get_cell_value() == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(6, clicked_row, clicked_col, screen)
                    if event.key == pygame.K_7:
                        if Sudoku_board.board[clicked_row][clicked_col].get_cell_value() == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(7, clicked_row, clicked_col, screen)
                    if event.key == pygame.K_8:
                        if Sudoku_board.board[clicked_row][clicked_col].get_cell_value() == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(8, clicked_row, clicked_col, screen)
                    if event.key == pygame.K_9:
                        if Sudoku_board.board[clicked_row][clicked_col].get_cell_value() == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(9, clicked_row, clicked_col, screen)

                    if event.key == pygame.K_BACKSPACE:
                        if Sudoku_board.sud_board[clicked_row][clicked_col] == 0:
                            Sudoku_board.board[clicked_row][clicked_col] = Cell(0, clicked_row, clicked_col, screen)

                    # for i in range(9):  # Put values onto board
                    #     for j in range(9):
                    #         Sudoku_board.board[i][j].draw()
                    screen.fill(BG_COLOR)  # Creates a white screen
                    Sudoku_board.draw()  # Draws the board (grids)
                    for i in range(9):  # Put values onto board
                        for j in range(9):
                            Sudoku_board.board[i][j].draw()

                    # Printing reset, restart, and exit buttons
                    button_font = pygame.font.Font(None, 70)
                    # Initialize buttons
                    # Initialize text first
                    reset_text = button_font.render("RESET", 0, (255, 255, 255))
                    restart_text = button_font.render("RESTART", 0, (255, 255, 255))
                    exit_text = button_font.render("EXIT", 0, (255, 255, 255))
                    # Initialize button background color and text
                    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
                    reset_surface.fill(LINE_COLOR)
                    reset_surface.blit(reset_text, (10, 10))
                    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
                    restart_surface.fill(LINE_COLOR)
                    restart_surface.blit(restart_text, (10, 10))
                    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
                    exit_surface.fill(LINE_COLOR)
                    exit_surface.blit(exit_text, (10, 10))
                    # Initialize button rectangle
                    reset_rectangle = reset_surface.get_rect(
                        center=(WIDTH // 2 - 250, HEIGHT - 100))
                    restart_rectangle = restart_surface.get_rect(
                        center=(WIDTH // 2, HEIGHT - 100))
                    exit_rectangle = exit_surface.get_rect(
                        center=(WIDTH // 2 + 250, HEIGHT - 100))
                    # Draw buttons
                    screen.blit(reset_surface, reset_rectangle)
                    screen.blit(restart_surface, restart_rectangle)
                    screen.blit(exit_surface, exit_rectangle)

                    if clicked_col <= 8 and clicked_row <= 8:
                        draw_selected_cell(clicked_row, clicked_col, WHITE_LINE_COLOR, SELECTED_CELL_LINE_WIDTH)
                        Sudoku_board.draw()  # Draws the board (grids)
                    if clicked_col <= 8 and clicked_row <= 8:
                        draw_selected_cell(clicked_row, clicked_col, SELECTED_CELL_LINE_COLOR, SELECTED_CELL_LINE_WIDTH)

                if event.type == pygame.KEYUP:
                    if check_full(screen) is True:
                        if check_boxes(screen) is True:
                            if check_col(screen) is True:
                                if check_row(screen) is True:
                                    winner = True
                                    g = False
                                    draw_game_over(screen)
                                    # Printing reset, restart, and exit buttons
                                    button_font = pygame.font.Font(None, 70)
                                    # Initialize buttons
                                    # Initialize text first
                                    exit_text = button_font.render("EXIT", 0, (255, 255, 255))
                                    # Initialize button background color and text
                                    exit_surface = pygame.Surface(
                                        (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
                                    exit_surface.fill(LINE_COLOR)
                                    exit_surface.blit(exit_text, (10, 10))
                                    # Initialize button rectangle
                                    exit_rectangle = exit_surface.get_rect(
                                        center=(WIDTH // 2 + 250, HEIGHT - 100))
                                    # Draw buttons
                                    screen.blit(exit_surface, exit_rectangle)
                        g = False
                        draw_game_over(screen)
                        # Printing reset, restart, and exit buttons
                        button_font = pygame.font.Font(None, 70)
                        # Initialize buttons
                        # Initialize text first
                        restart_text = button_font.render("RESTART", 0, (255, 255, 255))
                        # Initialize button background color and text
                        restart_surface = pygame.Surface(
                            (restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
                        restart_surface.fill(LINE_COLOR)
                        restart_surface.blit(restart_text, (10, 10))
                        # Initialize button rectangle
                        restart_rectangle = restart_surface.get_rect(
                            center=(WIDTH // 2, HEIGHT - 200))
                        # Draw buttons
                        screen.blit(restart_surface, restart_rectangle)
            pygame.display.update()
