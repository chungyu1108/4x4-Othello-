from Players import *
import sys
import OthelloBoard


class GameDriver:

  def __init__(self,
               p1type="human",
               p2type="alphabeta",
               num_rows=4,
               num_cols=4,
               p1_eval_type=0,
               p1_prune=False,
               p2_eval_type=0,
               p2_prune=False,
               p1_depth=8,
               p2_depth=8):
    if p1type.lower() in "human":
      self.p1 = HumanPlayer('X')

    elif p1type.lower() in "alphabeta":
      self.p1 = AlphaBetaPlayer('X', p1_eval_type, p1_prune, p1_depth)

    else:
      print("Invalid player 1 type!")
      exit(-1)

    if p2type.lower() in "human":
      self.p2 = HumanPlayer('O')

    elif p2type.lower() in "alphabeta":
      self.p2 = AlphaBetaPlayer('O', p2_eval_type, p2_prune, p2_depth)

    else:
      print("Invalid player 2 type!")
      exit(-1)

    self.board = OthelloBoard.OthelloBoard(num_rows, num_cols, self.p1.symbol,
                                           self.p2.symbol)
    self.board.initialize()

  def display(self):
    print("Player 1 (", self.p1.symbol, ") score: ", \
            self.board.count_score(self.p1.symbol))

  def process_move(self, curr_player, opponent):
    invalid_move = True
    while (invalid_move):
      (col, row) = curr_player.get_move(self.board)
      if (not self.board.is_legal_move(col, row, curr_player.symbol)):
        print("Invalid move")
      else:
        print("Move:", [col, row], "\n")
        self.board.play_move(col, row, curr_player.symbol)
        return

  def run(self):
    current = self.p1
    opponent = self.p2
    self.board.display()

    cant_move_counter, toggle = 0, 0

    #main execution of game
    print("Player 1(", self.p1.symbol, ") move:")
    # Get a move, then display it in a while loop
    turn_count = 0
    while True:
      if self.board.has_legal_moves_remaining(current.symbol):
        turn_count += 1
        cant_move_counter = 0
        self.process_move(current, opponent)
        self.board.display()
      else:
        print("Can't move")
        if (cant_move_counter == 1):
          break
        else:
          cant_move_counter += 1
      toggle = (toggle + 1) % 2
      if toggle == 0:
        current, opponent = self.p1, self.p2
        print("Player 1(", self.p1.symbol, ") move:")
      else:
        current, opponent = self.p2, self.p1
        print("Player 2(", self.p2.symbol, ") move:")

    #decide win/lose/tie state
    state = self.board.count_score(self.p1.symbol) - self.board.count_score(
      self.p2.symbol)
    if (state == 0):
      print("Tie game!!")
    elif state > 0:
      print("Player 1 Wins!")
    else:
      print("Player 2 Wins!")
    print("turn count:", turn_count)
    print("total nodes seen by p1", self.p1.total_nodes_seen)
    print("total nodes seen by p2", self.p2.total_nodes_seen)
    print("p1 max depth: ", self.p1.max_depth)
    print("p2 max depth: ", self.p2.max_depth)


def main():
  board_size = 4
  game = GameDriver(sys.argv[1], sys.argv[2], board_size, board_size,
                    sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6],
                    sys.argv[7], sys.argv[8])
  game.run()


main()
