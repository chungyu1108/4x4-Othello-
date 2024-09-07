# Calculate the next move for the computer player using the Alpha-beta and Minimax algorithms. 
Since we will be using ASCII art to display the board, we will use the symbols X (for the dark player who goes first) and O (for the light player who goes second). A legal move would outflank the enemies pieces in a straight line with your own pieces. The result would turn the outflanked enemy pieces into yours. If a player has no legal move, then the turn passes to the opponent, and if both players cannot move, then the game ends. The win is determined by who has more pieces when the game ends. The game starts with X's at (column 1, row 1) and (column 2, row 2) and O's at (column 1, row 2) and (column2, row 1).

The command line allows you to select whether a player is a human player or a computer player. Note that the 4x4 game of Othello is asymmetric; the player moving second has a serious advantage over the player moving first. If the search is exhaustive, the computer player, when going second, should always either win or tie.

The specific things you need to implement for this assignment are:

Evaluation functions: The 4x4 version of Othello is small enough that we can generate the entire game tree while doing the Minimax search. However, you will also experiment with shallower searches with an evaluation function. If a terminal state is reached, give an evaluation of 0 for a tie, float("inf") if you win, -float("inf") if you lose. Implement the following 3 evaluation functions:
H0, Piece Difference: Number of your pieces - number of opponent's pieces
H1, Mobility:  Number of your legal moves - number of opponent's legal moves
H2: Design your own function
# 2. Successor function: 
You will also need to create a successor function. This function takes the current state of the game and generates all the successors that can be reached within one move of the current state.

# 3. Alpha-beta/Minimax function: 
Implement the alpha-beta function in the adversarial search lecture. You will need to implement the Max-Value and Min-Value functions, successor function and different evaluation functions as defined below. Also, you will need to terminate the search once it hits a certain depth defined by the depth parameter.

In addition to the functionality described above, you may need to implement some other code to do things like bookkeeping. You also will need to create a report described below.
