import copy

#The following has been excluded as no application is apparent

from enum import Enum
#"Directsion enum for the Othello Board"
# a = Direction.S; 
# a.name == 'NE' 
#>true

class Direction(Enum):
    N   = 1
    NE  = 2
    E   = 3
    SE  = 4
    S   = 5
    SW   = 6
    W   = 7
    NW  = 8

#global empty state
EMPTY = '.'


class Board:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        #Col x Row grid filled with "EMPTY"
        self.grid = [[EMPTY for x in range(cols)] for y in range(rows)]


    #PYTHON    #Duplicate a board with B2 = B1.cloneBoard()
    #THIS SERVES AS BOTH COPY CONSTRUCTOR AND ASSIGNMENT
    def cloneBoard(self):
        tmp = Board(self.cols, self.rows)
        tmp.grid = copy.deepcopy(self.grid)
        return tmp


    #empties grid. No other references will remain.
    def delete_grid(self):
        for x in range(len(self.grid)):
            del self.grid[x][:]
        del self.grid[:]


    def get_num_cols(self):
        return self.cols

    def get_num_rows(self):
        return self.rows

    def get_cell(self, col, row):
        if not self.is_in_bounds(col, row):
            return None
        else:
            return self.grid[col][row]

    def set_cell(self, col, row, val):
        if not self.is_in_bounds(col, row):
            return None
        else:
            self.grid[col][row] = val



    def is_cell_empty(self, col, row):
        if self.grid[col][row] == EMPTY:
            return True
        return False

    def is_in_bounds(self, col, row):
        if (0 <= col < self.cols) and (0<= row < self.rows):
            return True
        else:
            return False


    def display(self):
        string2 = '--' * self.cols
        print(string2)
        for r in range(0,self.rows):
            string = ''
            
            for c in range(0, self.cols):
                string += self.grid[c][r] + ' '
            print(string)
        print(string2)