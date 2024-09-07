from Board import * 



class OthelloBoard(Board):
    """Class for Othello board
    children: successor positions for the current position
    move: the previous move taken to get to the current position
    value: the evaluation of the current position"""
    def __init__(self, rows, cols, p1, p2):
        Board.__init__(self, rows, cols)
        self.p1_symbol = p1
        self.p2_symbol = p2
        self.children = []
        self.move = None
        self.value = None 

#PYTHON: this function is substitute for clone. call as New = Old.cloneOBoard()
    def cloneOBoard(self):
        # When making a new board with clone, call initialize afterwards
        tmp = OthelloBoard(self.cols, self.rows, self.p1_symbol, self.p2_symbol)
        tmp.grid = copy.deepcopy(self.grid)
        return tmp

    def initialize(self):
        self.set_cell(self.cols //2 -1, self.rows //2 -1,   self.p1_symbol)
        self.set_cell(self.cols //2,    self.rows //2,      self.p1_symbol)
        self.set_cell(self.cols //2 -1, self.rows //2,      self.p2_symbol)
        self.set_cell(self.cols //2,    self.rows //2 -1,   self.p2_symbol)

    def set_coords_in_direction(self, col, row, D):#D=direction
        if(D.name == 'N'):
            row += 1
        elif(D.name == 'NE'):
            col+=1
            row+=1
        elif(D.name == 'E'):
            col+=1
        elif(D.name == 'SE'):
            col+=1
            row-=1
        elif(D.name == 'S'):
            row-=1
        elif(D.name == 'SW'):
            col-=1
            row-=1
        elif(D.name == 'W'):
            col-=1
        elif(D.name == 'NW'):
            col-=1
            row+=1
        else:
            print("Invalid Direction.")
        return (col, row)

#Recursively travel in a direction
    def check_endpoint(self, col, row, symbol, d, match_symbol):#match is bool type
        if not self.is_in_bounds(col, row) or self.is_cell_empty(col,row):
            return False
        else:
            if(match_symbol):
                if(self.get_cell(col, row) == symbol):
                    return True
                else:
                    (next_col, next_row) = self.set_coords_in_direction(col, row, d)
                    return self.check_endpoint(next_col, next_row, symbol, d, match_symbol)
            else:
                if(self.get_cell(col, row) == symbol):
                    return False
                else:
                    (next_col, next_row) = self.set_coords_in_direction(col, row, d)
                    return self.check_endpoint(next_col, next_row, symbol, d, not match_symbol)

    def is_legal_move(self, col, row, symbol):
        result = False
        if(not self.is_in_bounds(col, row) or not self.is_cell_empty(col, row)):
            return False
        for d in Direction: #enum from board.py
            (next_col, next_row) = self.set_coords_in_direction(col, row, d)
            if(self.check_endpoint(next_col, next_row, symbol, d, False)):
                return True
        return False
        
    def flip_pieces_helper(self, col, row, symbol, d):
        if(self.get_cell(col, row) == symbol):
            return 0
        else:
            self.set_cell(col,row, symbol)
            (next_col, next_row) = self.set_coords_in_direction(col, row, d)
            return 1+ self.flip_pieces_helper(next_col, next_row, symbol, d)


    def flip_pieces(self, col, row, symbol):
        pieces_flipped = 0
        if(not self.is_in_bounds(col, row)):
            print("Flip Pieces bad params.")
            exit();
        for d in Direction:
            (next_col, next_row) = self.set_coords_in_direction(col,row,d)
            if(self.check_endpoint(next_col, next_row, symbol, d, False)):
                pieces_flipped += self.flip_pieces_helper(next_col, next_row, symbol, d);

        return pieces_flipped

    def has_legal_moves_remaining(self, symbol):
        # Checks if a player with symbol can make any moves
        for c in range (0, self.cols):
            for r in range (0, self.rows):
                if self.is_cell_empty(c, r) and self.is_legal_move(c, r, symbol):
                    return True
        return False

    def count_score(self, symbol):
        # Counts the number of pieces with symbol
        score = 0
        for c in range (0, self.cols):
            for r in range (0, self.rows):
                if self.grid[c][r] == symbol:
                    score+=1
        return score 

    def play_move(self, col, row, symbol):
        # Changes the board state with a move
        self.set_cell(col, row, symbol)
        self.flip_pieces(col, row, symbol)