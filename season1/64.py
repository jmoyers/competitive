"""
---
number: 64
title: Minimum Path Sum
difficulty: medium
tags:
- dynamic programming
- hash map
- minimum path
- dfs
- graph
---
Given a m x n grid filled with non-negative numbers, find a path from top
left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
from typing import List


class Solution:
    def __init__(self):
        self.grid = None
        self.memo = {}
        self.m = 0
        self.n = 0

    def _dfs(self, row, col, sum) -> int:
        if (row, col) in self.memo:
            return self.memo[(row, col)]

        sum_from_node = 0
        down = float("inf")
        right = float("inf")

        if row + 1 < self.m:
            down = self._dfs(row + 1, col, sum)
        if col + 1 < self.n:
            right = self._dfs(row, col + 1, sum)

        if right == float("inf") and down == float("inf"):
            self.memo[(row, col)] = self.grid[row][col]
            return self.grid[row][col]
        else:
            sum_from_node = min(right, down)
            self.memo[(row, col)] = self.grid[row][col] + sum_from_node
            return self.grid[row][col] + sum_from_node

    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        self.grid = grid

        self.m, self.n = len(grid), len(grid[0])

        return self._dfs(0, 0, 0)


def test_lc1():
    inp = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = Solution().minPathSum(inp)
    assert result == 7


def test_lc2():
    inp = [[1, 2, 5], [3, 2, 1]]
    result = Solution().minPathSum(inp)
