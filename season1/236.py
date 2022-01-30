"""
---
title: Lowest Common Ancestor of a Binary Tree
number: 236
tags:
- binary tree
- tree
links:
- https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
---
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree: root = [3,5,1,6,2,0,8,null,null,7,4]

https://assets.leetcode.com/uploads/2018/12/14/binarytree.png

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
of itself according to the LCA definition.

 

Note:

    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    First we need to find each of the nodes. Two choices are bfs and dfs --
    dfs is fine in this case as its going to take n time no matter what and
    bfs can be expensive in terms of memory.

    If we use an array to keep track of the visited nodes on the dfs path
    to the found node in p, we can then compare it to the visited nodes of
    the dfs path to node q.

    The first divergence means that is the first shared ancestor.
    """

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node: "TreeNode", val, path):
            if val == node.val:
                path.append(node)
                return True

            if node.left and dfs(node.left, val, path):
                path.append(node)
                return True

            if node.right and dfs(node.right, val, path):
                path.append(node)
                return True

        p_path, q_path = [], []

        dfs(root, p.val, p_path)
        dfs(root, q.val, q_path)

        q_path.reverse()
        p_path.reverse()

        longer = q_path if len(q_path) > len(p_path) else p_path
        shorter = q_path if longer == p_path else p_path

        for i, node in enumerate(longer):
            if node not in shorter:
                return longer[i - 1]


def make_tree() -> "TreeNode":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    return root


def test_lc1():
    assert (
        Solution().lowestCommonAncestor(make_tree(), TreeNode(5), TreeNode(1)).val == 3
    )


def test_lc2():
    assert (
        Solution().lowestCommonAncestor(make_tree(), TreeNode(5), TreeNode(4)).val == 5
    )
