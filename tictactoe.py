"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_x, number_of_o = 0, 0
    for list in board:
        number_of_x += list.count(X)
        number_of_o += list.count(O)
    if number_of_x > number_of_o: return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY: actions_set.add((i,j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp_board = copy.deepcopy(board)
    if temp_board[action[0]][action[1]] == EMPTY:
        temp_board[action[0]][action[1]] = player(temp_board)
        return temp_board
    else:
        raise Exception('The Action is not Valid!')

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            if board[i][0] == X: return X
            return O
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            if board[0][i] == X: return X
            return O
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        if board[1][1] == X: return X
        return O
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        if board[1][1] == X: return X
        return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY: return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X: return 1
        elif winner(board) == O: return -1
        return 0



def max_value(board):
    if terminal(board): return utility(board)
    else:
        maxv = -math.inf
        for action in actions(board):
            maxv = max(maxv, min_value(result(board, action)))
        return maxv

def min_value(board):
    if terminal(board): return utility(board)
    else:
        minv =  math.inf
        for action in actions(board):
            minv = min(minv, max_value(result(board, action)))
        return minv
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            plays = []
            for action in actions(board):
                plays.append((min_value(result(board,action)), action))
            return sorted(plays, key = lambda x: x[0], reverse = True)[0][1]
        else:
            plays = []
            for action in actions(board):
                plays.append((max_value(result(board,action)), action))
            return sorted(plays, key = lambda x: x[0])[0][1]
