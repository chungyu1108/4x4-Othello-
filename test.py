# Basic test file example

from Players import *
from GameDriver import GameDriver
import unittest
import pdb


class testPlayers(unittest.TestCase):
  """This class tests the Players.py file"""

  def test_successors(self):
    game = GameDriver(p1type="alphabeta",
                      p2type="alphabeta",
                      num_rows=4,
                      num_cols=4,
                      p1_eval_type=0,
                      p1_prune=0,
                      p2_eval_type=0,
                      p2_prune=0,
                      p1_depth=12,
                      p2_depth=12)
    successors = game.p1.get_successors(game.board, "X")
    self.assertEqual(len(successors), 4)

  def test_eval(self):
    game = GameDriver(p1type="alphabeta",
                      p2type="alphabeta",
                      num_rows=4,
                      num_cols=4,
                      p1_eval_type=0,
                      p1_prune=0,
                      p2_eval_type=0,
                      p2_prune=0,
                      p1_depth=12,
                      p2_depth=12)
    print("Starting board")
    game.board.display()
    successors = game.p1.get_successors(game.board, "X")
    current = game.p1
    s = successors[0]
    print("First move by player 1")
    s.display()
    current.eval_type = '0'
    eval0 = current.eval_board(s)
    print("eval0 piece difference", eval0)
    self.assertEqual(eval0, 3)
    current.eval_type = '1'
    eval1 = current.eval_board(s)
    print("eval1 mobility difference", eval1)
    self.assertEqual(eval1, 0)
    #pdb.set_trace()


if __name__ == "__main__":
  unittest.main()
