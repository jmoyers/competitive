"""
---
number: 695
title: Max Area of Island
difficulty: medium
---

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You
may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no
island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island
must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
from typing import List
import math


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        self.max_area = -math.inf
        self.R, self.C = len(grid), len(grid[0])
        self.grid = grid

        self.area = 0

        for i in range(self.R):
            for j in range(self.C):
                self.area = 0
                self.dfs(i, j)
                self.max_area = max(self.area, self.max_area)
        return self.max_area

    def dfs(self, r, c):
        # 4 directional
        if self.grid[r][c] == 1:
            self.grid[r][c] = 0
            self.area += 1
        else:
            return

        # left
        if c - 1 >= 0:
            self.dfs(r, c - 1)
        # right
        if c + 1 < self.C:
            self.dfs(r, c + 1)
        # down
        if r + 1 < self.R:
            self.dfs(r + 1, c)
        # up
        if r - 1 >= 0:
            self.dfs(r - 1, c)

