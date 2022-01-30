"""
---
number:98
title:Validate Binary Search Tree
difficulty:medium
tags:
- binary search tree
- validation
- depth first search
- recursion
---
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _dfs(self, node: TreeNode, less, greater) -> bool:
        if not node:
            return True

        if less is not None:
            if node.val >= less:
                return False

        if greater is not None:
            if node.val <= greater:
                return False

        if not self._dfs(node.left, node.val, greater):
            return False

        if not self._dfs(node.right, less, node.val):
            return False

        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self._dfs(root, None, None)


def test_lc1():
    r = TreeNode(2, TreeNode(1), TreeNode(3))
    assert Solution().isValidBST(r)


def test_lc2():
    r = TreeNode(2, TreeNode(3), TreeNode(4))
    assert Solution().isValidBST(r) == False
