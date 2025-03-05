import math
import random


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = int(row_length)
        self.removed_cells = int(removed_cells)
        self.box_length = int(math.sqrt(self.row_length))
        self.board = []
        self.answer = None
        for i in range(self.row_length):
            row = []
            for j in range(self.row_length):
                row.append(0)
            self.board.append(row)

    def get_board(self):  # WORKS
        # Returns a 2D python list of numbers, which represents the board
        # Parameters: None
        # Return: list[list]
        return self.board

    def print_board(self):  # WORKS
        # Displays the board to the console
        # This is not strictly required, but it may be useful for debugging purposes
        # Parameters: None
        # Return: None
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()

    def valid_in_row(self, row, num):  # WORKS
        # Determines if num is contained in the specified row (horizontal) of the board
        # If num is already in the specified row, return False. Otherwise, return True
        # Parameters:
        #   row is the index of the row we are checking
        # 	num is the value we are looking for in the row
        # Return: boolean
        # NOTES: self.board[row number][column number]
        for i in range(self.row_length):
            if self.board[row][i] == num:
                return False
        return True

    def valid_in_col(self, col, num):  # WORKS
        # Determines if num is contained in the specified column (vertical) of the board
        # If num is already in the specified col, return False. Otherwise, return True
        # Parameters:
        #   col is the index of the column we are checking
        #   num is the value we are looking for in the column
        # Return: boolean
        for i in range(self.row_length):
            if self.board[i][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):  # WORKS
        # Determines if num is contained in the 3x3 box specified on the board
        # If num is in the specified box starting at (row_start, col_start), return False.
        # Otherwise, return True
        # Parameters:
        # 	row_start and col_start are the starting indices of the box to check
        # 	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
        # 	num is the value we are looking for in the box
        # Return: boolean
        box_row = row_start - row_start % int(self.box_length)  # Makes sure a box index never goes out of range
        # Alters index so no matter the index we put in it is the start of a 3x3 square
        box_col = col_start - col_start % int(self.box_length)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if num == self.board[i][j]:
                    return False
        return True

    def is_valid(self, row, col, num):  # WORKS
        # Determines if it is valid to enter num at (row, col) in the board
        # This is done by checking that num is unused in the appropriate, row, column, and box
        # Parameters:
        #   row and col are the row index and col index of the cell to check in the board
        #   num is the value to test if it is safe to enter in this cell
        # return boolean
        if self.valid_in_row(row, num) is False:
            return False
        elif self.valid_in_col(col, num) is False:
            return False
        elif self.valid_in_box(row, col, num) is False:
            return False
        else:
            return True

    def fill_box(self, row_start, col_start):  # WORKS
        # Fills the specified 3x3 box with values
        # For each position, generates a random digit which has not yet been used in the box
        # Parameters:
        #   row_start and col_start are the starting indices of the box to check
        # 	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
        # Return: None
        # self.board[row number][column number]
        random_lst = []
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                while True:
                    num_1 = random.randint(1, 9)
                    if num_1 in random_lst:
                        continue
                    else:
                        self.board[i][j] = num_1
                        random_lst.append(num_1)
                        break

    def fill_diagonal(self):  # WORKS
        # Fills the three boxes along the main diagonal of the board
        # These are the boxes which start at (0,0), (3,3), and (6,6)
        # Parameters: None
        # Return: None
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):  # WORKS
        # DO NOT CHANGE
        # Provided for students
        # Fills the remaining cells of the board
        # Should be called after the diagonal boxes have been filled
        # Parameters: row, col specify the coordinates of the first empty (0) cell
        # Return: boolean (whether we could solve the board)
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):  # WORKS
        # DO NOT CHANGE
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):  # Cole
        # This method removes the appropriate number of cells from the board.
        # It does so by randomly generating (row, col) coordinates of the board and setting the value to 0.
        for i in range(0, self.removed_cells):  # The number of cells we want to remove
            while True:  # While loop that ends when we find a filled cell
                random_row = random.randint(0, 8)  # Random numbers [0, 8]
                random_col = random.randint(0, 8)
                if self.board[random_row][random_col] != 0:  # A filled cell will not have 0 as its value
                    self.board[random_row][random_col] = 0
                    break
                else:
                    continue


def generate_sudoku(size, removed):  # WORKS
    # DO NOT CHANGE
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()

    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
