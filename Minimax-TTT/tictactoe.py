"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY , EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    if board == initial_state():
	    return X
    numx = 0
    numo = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                numx = numx + 1
            if board[i][j] == O:
                numo = numo + 1

    if numx > numo:
        return O
    else:
	    return X
    
def actions(board):
    possiblemoves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possiblemoves.add((i,j))
    return possiblemoves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] not in range(0, 3) or action[1] not in range(0, 3) or board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")
    
    copyboard = [row[:] for row in board]

    copyboard[ action[0] ][ action[1] ] = player(board)
    return copyboard
"""
def horizontal(board):
    for x in range(3):
        if (board[x][0] == board[x][1] and board[x][1] == board[x][2]) and board[x][0] != None:
            pl = board[x][0]
            return pl
    
        return None

def vertical(board):
    for y in range(3):
        if (board[0][y] == board[1][y] and board[1][y] == board[2][y]) and board[1][y] != None:
            pl = board[1][y]
            return pl
    return None

def diagonally(board):
    if (board[0][0] == board[1][1] and board[1][1]==board[2][2]) and board[0][0] != None:
        return board[0][0]
    if (board[0][2] == board[1][1] and board[1][1]==board[2][0]) and board[0][2] != None:
        return board[0][2]
    else:
        return None

"""
def winner(board):
    # Check rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None
def arethereanyspace(board):
    space = 0
    for row in board:
        for item in row:
            if item == EMPTY:
                space +=1

    return space

def tie(board):
    if winner(board) == None and arethereanyspace(board) == 0:
        return True
    else:
        return False
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if tie(board): 
        return True
    
    if winner(board) is not None:
        return True
    
    else:
        return False


def utility(board):

    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0
 
def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    """

    if terminal(board):
        return None

    if player(board) == X:#maximizer
        maxi = -2 #worst than the worst
        for a in actions(board):
            maxval = minvalue(result(board,a))
            if maxval > maxi:
                maxi = maxval
                bestmove = a

    else:#minimizer
        mini = +2 #better then the best
        for a in actions(board):
            minval = maxvalue(result(board,a))
            if minval < mini:
                mini = minval
                bestmove = a

    return bestmove

def minvalue(board):
    if terminal(board):
        return utility(board)

    v = +2
    for action in actions(board):
        v = min(v, maxvalue(result(board,action)))
    return v

def maxvalue(board):
    if terminal(board):
        return utility(board)

    v = -2
    for action in actions(board):
        v = max(v, minvalue(result(board,action)))
    return v
