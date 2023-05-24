from __future__ import annotations
from board import Board
from collections.abc import Callable
from queue import PriorityQueue
import copy

class BoardState:
    def __init__(self, board: Board, move: str, pastMoves):
        self.board = board
        self.pastMoves = copy.deepcopy(pastMoves)

        if move != '':
            self.pastMoves.append(move)

    def Seen(self, seenDict):

        if len(seenDict) == 0:
            return False

        if str(self.board) in seenDict:
            if len(seenDict[str(self.board)]) <= len(self.pastMoves):
                return True
            else:
                return False

'''
Heuristics
'''
def MT(board: Board) -> int:
    solStr = "[[1 2 3]\n [4 5 6]\n [7 8 0]]"
    return sum(1 for a, b in zip(str(board), solStr) if a != b)

def CB(board: Board) -> int:
    sol = {0: (2, 2), 1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (0, 1), 5: (1, 1), 6: (2, 1), 7: (0, 2), 8: (1, 2)}
    total = 0

    for y, row in enumerate(board.state):
        for x, num in enumerate(row):
            total += (abs(sol[num][0] - x) + abs(sol[num][1] - y))

    return total

def NA(board: Board) -> int:
    return 9 - MT(board) # Returns the number of correct squares

def BFS(board: Board) -> int:
    return 0



'''
A* Search 
'''
def a_star_search(board: Board, heuristic: Callable[[Board], int]):
    frontier = PriorityQueue()
    seen = {}
    currState = BoardState(board, "", [])
    numNodesSearched = 0

    # While the board is not in a goal state
    while not currState.board.goal_test():
        for possibleMove in currState.board.next_action_states(): # Iterate over all possible moves
            newState = BoardState(possibleMove[0], possibleMove[1], currState.pastMoves) # Create a new board state for this move

            if not newState.Seen(seen): # Check if this string has been seen before
                priority = len(newState.pastMoves) + heuristic(newState.board)
                frontier.put((priority, id(newState), newState)) # ID is there to be a tie breaker in case of identical priorities
                seen[str(newState.board)] = newState.pastMoves

        currState = frontier.get()[2]
        numNodesSearched += 1

    return (numNodesSearched, currState.pastMoves)
    # return currState.pastMoves <- This is for running with test.py
