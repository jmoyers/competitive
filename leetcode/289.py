"""
---
title: Game of Life
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/game-of-life
---
According to the Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician John
Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or
dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
diagonal) using the following four rules (taken from the above Wikipedia
article):

    Any live cell with fewer than two live neighbors dies, as if caused by
    under-population.

    Any live cell with two or three live neighbors lives on to the next
    generation.

    Any live cell with more than three live neighbors dies, as if by
    over-population..

    Any dead cell with exactly three live neighbors becomes a live cell, as if by
    reproduction.

Write a function to compute the next state (after one update) of the board
given its current state. The next state is created by applying the above
rules simultaneously to every cell in the current state, where births and
deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated at
    the same time: You cannot update some cells first and then use their updated
    values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the
    board is infinite, which would cause problems when the active area encroaches
    the border of the array. How would you address these problems?
"""
from typing import List


class Solution:
    """
    The solution is to keep a copy of the game board. Pretty simple.

    If you're trying to do it "in place" you still need 4 states, which means the
    input cells can't be a boolean (1 bit). But if your input cells are some goofy
    scripted language with either a string or a int input cell type, then you
    can store the state as some other number or letter.

    You need to know if a now-dead cell was alive or if a now-alive cell was dead. So
    you can compute its neighboring cells by its old state. So you can use a letter or
    number repesenting each of those states.

    As for an "infinite board" -- perhaps due to the nature of the game, you don't have
    all that much life after all, so you could represent the matrix as a dictionary of
    states where the key is the cell position (tuple key). This is the same concept as
    using whitespace collapsing in compression.

    I will just implement the board copy here.
    """

    def gameOfLifeCopy(self, board: List[List[int]]) -> None:
        if not board or not board[0]:
            return

        cp = [row[:] for row in board]

        for r in range(len(board)):
            for c in range(len(board[0])):
                neighbors = 0

                for x, y in (
                    (r, c - 1),
                    (r - 1, c - 1),
                    (r - 1, c),
                    (r - 1, c + 1),
                    (r, c + 1),
                    (r + 1, c + 1),
                    (r + 1, c),
                    (r + 1, c - 1),
                ):
                    if not 0 <= x < len(board):
                        continue

                    if not 0 <= y < len(board[0]):
                        continue

                    if cp[x][y] == 1:
                        neighbors += 1

                if neighbors < 2:
                    board[r][c] = 0
                elif neighbors <= 3 and cp[r][c] == 1:
                    board[r][c] = 1
                elif neighbors > 3 and cp[r][c] == 1:
                    board[r][c] = 0
                elif neighbors == 3:
                    board[r][c] = 1

    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                neighbors = 0

                for x, y in (
                    (r, c - 1),
                    (r - 1, c - 1),
                    (r - 1, c),
                    (r - 1, c + 1),
                    (r, c + 1),
                    (r + 1, c + 1),
                    (r + 1, c),
                    (r + 1, c - 1),
                ):
                    if not 0 <= x < m:
                        continue

                    if not 0 <= y < n:
                        continue

                    if board[x][y] in (-1, 1):
                        neighbors += 1

                # alive or was alive 1, -1
                # dead or was dead 0, 2

                if board[r][c] == 1:
                    # underpop
                    if neighbors < 2:
                        board[r][c] = -1
                    # stable
                    elif neighbors <= 3:
                        board[r][c] = 1
                    # overpop
                    elif neighbors > 3:
                        board[r][c] = -1
                # reproduction
                elif neighbors == 3:
                    board[r][c] = 2

        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0


def test_1():
    input = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    output = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    Solution().gameOfLife(input)

    assert input == output


if __name__ == "__main__":
    test_1()
