"""
---
title: Spiral Matrix
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/spiral-matrix
---
Given a matrix of m x n elements (m rows, n columns), return all elements of
the matrix in spiral order.
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        startRow, startCol = 0, 0
        endRow: int = len(matrix) - 1
        endCol: int = len(matrix[0]) - 1

        result: List[int] = []

        while startRow <= endRow and startCol <= endCol:

            # right - increasing col
            for col in range(startCol, endCol + 1):
                result.append(matrix[startRow][col])

            startRow += 1

            # down - increasing row
            for row in range(startRow, endRow + 1):
                result.append(matrix[row][endCol])

            endCol -= 1

            # btw you need this conditionals for both non-square
            # matricies and to prevent processing a row or
            # column more than once
            if startRow <= endRow:
                # left - decresing col - processing a row
                for col in range(endCol, startCol - 1, -1):
                    result.append(matrix[endRow][col])

            endRow -= 1

            if startCol <= endCol:
                # up - decreasing row - processing a column
                for row in range(endRow, startRow - 1, -1):
                    result.append(matrix[row][startCol])

            startCol += 1

        return result


result = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)
assert result == [1, 2, 3, 6, 9, 8, 7, 4, 5]

result = Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(result)
assert result == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

result = Solution().spiralOrder([[1, 2, 3, 4],])
print(result)
assert result == [1, 2, 3, 4]

result = Solution().spiralOrder([[1], [2], [3], [4], [5]])
print(result)
assert result == [1, 2, 3, 4, 5]
