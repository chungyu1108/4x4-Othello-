from OthelloBoard import OthelloBoard


class Player:
  """Base player class"""

  def __init__(self, symbol):
    self.symbol = symbol

  def get_symbol(self):
    return self.symbol

  def get_move(self, board):
    raise NotImplementedError("Subclasses must implement the get_move method.")


class HumanPlayer(Player):
  """Human subclass with text input in command line"""

  def __init__(self, symbol):
    Player.__init__(self, symbol)

  def get_move(self, board):
    col = int(input("Enter col: "))
    row = int(input("Enter row: "))
    return col, row


class AlphaBetaPlayer(Player):
  """Class for Alphabeta AI: implement functions minimax, eval_board, get_successors, get_move
    eval_type: int
        0 for H0, 1 for H1, 2 for H2
    prune: bool
        1 for alpha-beta, 0 otherwise
    max_depth: one move makes the depth of a position to 1, search should not exceed depth
    symbol: X for player 1 and O for player 2
    """

  def __init__(self, symbol, eval_type, prune, max_depth):
    Player.__init__(self, symbol)
    self.eval_type = eval_type
    self.prune = prune
    self.max_depth = int(max_depth)
    self.max_depth_seen = 0
    self.total_nodes_seen = 0
    if symbol == 'X':
      self.oppSym = 'O'
    else:
      self.oppSym = 'X'

  def terminal_state(self, board):
    # If either player can make a move, it's not a terminal state
    for c in range(board.cols):
      for r in range(board.rows):
        if board.is_legal_move(c, r, "X") or board.is_legal_move(c, r, "O"):
          return False
    return True

  def terminal_value(self, board):
    # Regardless of X or O, a win is float('inf')
    state = board.count_score(self.symbol) - board.count_score(self.oppSym)
    if state == 0:
      return 0
    elif state > 0:
      return float('inf')
    else:
      return -float('inf')

  def flip_symbol(self, symbol):
    # Short function to flip a symbol
    if symbol == "X":
      return "O"
    else:
      return "X"

  def alphabeta(self, board, alpha, beta, depth, max_player):
    if depth == self.max_depth or self.terminal_state(board):
      print("this is max depth or terminal state")
      return self.eval_board(board)

    if max_player:
      print("This is max player")
      value = float('-inf')
      successors = self.get_successors(board, self.symbol)
      for successor in successors:
        self.max_depth_seen += 1
        new_board = board.play_move(successor[0], successor[1], self.symbol)
        value = max(value,
                    self.alphabeta(new_board, alpha, beta, depth + 1, False))
        alpha = max(alpha, value)
        if self.prune and beta <= alpha:
          break
      return value
    else:
      print("This is min player")
      value = float('inf')
      successors = self.get_successors(board, self.oppSym)
      for successor in successors:
        self.max_depth_seen += 1
        new_board = board.play_move(successor[0], successor[1], self.oppSym)
        value = min(value,
                    self.alphabeta(new_board, alpha, beta, depth + 1, True))
        beta = min(beta, value)
        if self.prune and beta <= alpha:
          break
      return value

  def eval_board(self, board):
    print("self.eval_type: " + self.eval_type)
    if self.eval_type == str(0):
      print("type is H0")
      return self.eval_h0(board)
    elif self.eval_type == 1:
      print("type is H1")
      return self.eval_h1(board)
    elif self.eval_type == 2:
      print("type is H2")
      return self.eval_h2(board)
    
  def eval_h0(self, board):
    return board.count_score(self.symbol) - board.count_score(self.oppSym)

  def eval_h1(self, board):
    return len(self.get_successors(board, self.symbol)) - len( self.get_successors(board, self.oppSym))

  def eval_h2(self, board):
     # Calculate the difference in the number of pieces between the players
    player_score = board.count_score(self.symbol)
    opponent_score = board.count_score(self.oppSym)
    score_diff = player_score - opponent_score

    # Assign a higher score if the player has more pieces, lower score otherwise
    if score_diff > 0:
        return score_diff
    elif score_diff < 0:
        return -score_diff
    else:
        return 0

  def get_successors(self, board, player_symbol):
    successors = []
    for c in range(board.cols):
      for r in range(board.rows):
        if board.is_legal_move(c, r, player_symbol):
          successors.append((c, r))
    return successors

  def get_move(self, board):
    new_board = OthelloBoard(board.get_num_rows(), board.get_num_cols(), self.symbol, self.oppSym)
    best_move = None
    best_score = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    depth = 0
    max_player = True

    successors = self.get_successors(board, self.symbol)
    for move in successors:
      new_board_copy = new_board.cloneOBoard()
      new_board_copy.play_move(move[0], move[1], self.symbol)
      score = self.alphabeta(new_board_copy, alpha, beta, depth + 1, max_player)
      if score > best_score:
        best_score = score
        best_move = move
      alpha = max(alpha, best_score)

    return best_move
