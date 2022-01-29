"""
---
title: Binary Search Tree Iterator
difficulty: medium
level: 2
links: 
- https://leetcode.com/problems/binary-search-tree-iterator
---
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: "TreeNode"):
        self.values = []
        self.dfs(root)
        self.values.sort(reverse=True)

    def dfs(self, node):
        if not node:
            return
        self.values.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)

    def next(self) -> int:
        return self.values.pop()

    def hasNext(self) -> bool:
        return len(self.values) > 0
