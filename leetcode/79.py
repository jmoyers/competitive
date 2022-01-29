"""
---
title: Word Search
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/word-search
---
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3

"""
from typing import List, Dict, Tuple

from collections import defaultdict


class Solution:
    """
    Seems like the straightforward solution is a DFS beginning every time
    there is a cell with a starting letter in it that searches for a character
    in the word with an index incrementing every time a letter is found.

    We would update a visited dict every time we visit a new cell and encounter 
    a the letter we're currently search for, and if we fail at some point in the
    dfs, the visited dict gets set to false as the stack unwinds.

    After testing, building up a visited dictionary and updating is quite
    quite expensive on some larger test data sets. Its a bit faster just to
    mark our path by modifying the board inline, so we do that below.

    There is a commit with the arguably easier to understand dictionary solution
    right before this.
    """

    def exist(self, board: List[List[str]], word: str) -> bool:

        curr_index = 0

        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(r, c, curr_index, word, board):
                    return True
        return False

    def dfs(self, r: int, c: int, curr_index, word, board) -> bool:

        if board[r][c] == word[curr_index]:
            curr_index += 1
            tmp, board[r][c] = board[r][c], "-"

            # base case
            if curr_index == len(word):
                return True

            for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if not 0 <= x < len(board) or not 0 <= y < len(board[0]):
                    continue

                if self.dfs(x, y, curr_index, word, board):
                    board[r][c] = tmp
                    return True

            board[r][c] = tmp
            curr_index -= 1

        # no linked cell produced a match, unwind
        return False


def test_1():
    input = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert Solution().exist(input, "ABCCED")
    assert Solution().exist(input, "SEE")
    assert not Solution().exist(input, "ABCB")
