"""
Given a binary tree, return the vertical order traversal of its nodes'
values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to
right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left
child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_left = 0
        self.max_right = 0
        self.max_depth = 0

    def find_dims(self, node, depth=0, column=0) -> None:
        """
        Do a dfs, find the width of tree. Discover what column the
        root of the tree lies in.
        """
        if not node:
            return

        self.min_left = min(column, self.min_left)
        self.max_right = max(column, self.max_right)
        self.max_depth = max(depth, self.max_depth)

        if node.left:
            self.find_dims(node.left, depth + 1, column - 1)
        if node.right:
            self.find_dims(node.right, depth + 1, column + 1)

    def place_values(self, node, column, results) -> None:
        """
        Do a bfs to guarantee depth order left-to-right
        """
        queue = deque([(node, column)])

        while queue:
            node, new_col = queue.popleft()

            if node == "col_reset":
                column = new_col
                continue

            column = new_col

            results[column].append(node.val)

            if node.left:
                queue.append((node.left, column - 1))
            if node.right:
                queue.append((node.right, column + 1))
            queue.append(("col_reset", column))

    def verticalOrder(self, root: "TreeNode") -> List[List[int]]:
        if not root:
            return []
        # first pass, establish tree dimensions and figure out
        # "where" the root is given those dimensions
        self.find_dims(root)
        width = self.max_right - self.min_left + 1
        results = [[] for _ in range(width)]

        self.place_values(root, abs(self.min_left), results)
        return results


def test_lc1():
    inp = TreeNode(2, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = Solution().verticalOrder(inp)


def test_lc2():
    inp = TreeNode(
        3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7))
    )
    result = Solution().verticalOrder(inp)
    assert result == [[4], [9], [3, 0, 1], [8], [7]]


# [3,9,8,4,0,1,7,null,null,null,2,5]

#         3
#      9     8
#   4    01      7
#        25
