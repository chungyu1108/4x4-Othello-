#!/bin/sh
#p1type="human", p2type="minimax", p1_eval_type=0, p1_prune=False, p2_eval_type=0, p2_prune=False

# python GameDriver.py human human 0 0 0 0 8 8
# python GameDriver.py human alphabeta 0 0 0 0 8 8
python GameDriver.py alphabeta alphabeta 0 0 0 0 8 8