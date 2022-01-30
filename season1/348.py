"""
---
title: Design Tic-Tac-Toe
difficulty: medium
level: 2
tags:
- dynamic programming
- game
- array
links: 
- https://leetcode.com/problems/design-tic-tac-toe
---
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

    A move is guaranteed to be valid and is placed on an empty block.

    Once a winning condition is reached, no more moves is allowed.
    A player who succeeds in placing n of their marks in a horizontal,
    vertical, or diagonal row wins the game.

Example:

Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

Follow up:
Could you do better than O(n^2) per move() operation? 
"""


class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.board = [[None] * n for i in range(n)]

        # all possible win sequences, first n all columns, second n all rows,
        # last 2 are diagnal win conditions

        # this is just a plain ol' dynamic programming approach
        self.seq = [[0 for i in range(n + n + 2)] for i in range(2)]

    def is_diag(self, x, y) -> (bool, bool):
        # n = 3
        # 0, 2 -- y = n - 1 - x
        # 1, 1 -- y = 3 - 1 - 1
        # 2, 0 -- y = 3 - 1 - 2

        r = [False, False]

        if x == y:
            r[0] = True
        if y == self.n - 1 - x:
            r[1] = True

        return (r[0], r[1])

    def move(self, x, y, p):
        mark = "X" if p == 1 else "O"
        n = self.n

        self.board[y][x] = mark

        self.seq[p - 1][x] += 1

        if self.seq[p - 1][x] == n:
            return p

        self.seq[p - 1][n + y] += 1

        if self.seq[p - 1][n + y] == n:
            return p

        d1, d2 = self.is_diag(x, y)

        if d1:
            self.seq[p - 1][n + n] += 1
            if self.seq[p - 1][n + n] == n:
                return p

        if d2:
            self.seq[p - 1][n + n + 1] += 1
            if self.seq[p - 1][n + n + 1] == n:
                return p

        return 0


def test_tic_tac():
    t = TicTacToe(4)
    assert t.move(0, 0, 2) == 0
    assert t.move(1, 1, 2) == 0
    assert t.move(2, 2, 2) == 0
    assert t.move(3, 3, 2) == 2


def test_lc1():
    t = TicTacToe(2)
    assert t.move(0, 1, 1) == 0
    assert t.move(1, 1, 2) == 0
    assert t.move(1, 0, 1) == 1


def test_lc2():
    t = TicTacToe(3)
    assert t.move(1, 1, 2) == 0
    assert t.move(0, 2, 2) == 0
    assert t.move(2, 0, 2) == 2
