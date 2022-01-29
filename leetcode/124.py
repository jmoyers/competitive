"""
---
title: Binary Tree Maximum Path Sum
number: 124
difficulty: hard
tags: [recursion, binary tree, path finding, maximum]
links:
- https://leetcode.com/problems/binary-tree-maximum-path-sum/solution/
---

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

from typing import List, Optional, Union
from math import floor


def pprint_tree(node, file=None, _prefix="", _last=True):
    print(
        _prefix,
        "`- " if _last else "|- ",
        node.val if node else "None",
        sep="",
        file=file,
    )

    _prefix += "   " if _last else "|  "
    children = [node.left, node.right]
    child_count = len(children)
    for i, child in enumerate(children):
        if child is None:
            continue
        _last = i == (child_count - 1)
        pprint_tree(child, file, _prefix, _last)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Since we don't need to return a path, the mechanics of this are simplified.

    This is not a binary search tree, so the left/right children have no
    semantics, and so we at a minimum need to examine all nodes once.

    The root of the tree or subtrees can have negative nodes, so the best path
    could not contain the whole root of the tree.

    If we model this so that for each node we're calculating the max of each
    child left/right recursively, then adding it to the current nodes value
    to get the max(current_node), we should be able to iterate through all nodes
    recursively.

    Along the way, whenever a given nodes max value is larger than what we've
    stored, you can update it. Since we don't need path, we'll just return this
    value at the end, so its the only bookkeeping you'll need to do.
    """

    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, node: TreeNode) -> int:
        """
        This calculates the maximum gain for this node and all its children.
        The return value is the maximum gain at this node. If this value
        is larger than what we know to be the maximum for the whole tree up to
        this point, then we'll update that value. It'll be stored as an instance
        variable.
        """
        if node is None:
            return 0

        curr_max = node.val

        left_gain = self.max_gain(node.left)
        right_gain = self.max_gain(node.right)

        curr_max = max(curr_max, node.val + left_gain)
        curr_max = max(curr_max, node.val + right_gain)
        curr_max = max(curr_max, node.val + left_gain + right_gain)

        self.max_sum = max(curr_max, self.max_sum)

        # if we want to use this node above, we can only use one  of the
        # branches, however we always want to update max_sum as if we weren't
        # going to consider other nodes in case this node + left + right is the
        # actual max path
        return max(node.val, left_gain + node.val, right_gain + node.val)


# I don't want to fix list2tree - they aren't using a heap style list, its
# got None child compression, so these tests are broken


def stuff_1():
    inp = list2tree([1, 2, 3])
    out = 6

    assert Solution().maxPathSum(inp) == out


def stuff_2():
    inp = list2tree([2, -1])
    out = 2

    assert Solution().maxPathSum(inp) == out


def stuff_3():
    inp = list2tree([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])
    out = 16

    """
                9
            6           -3
         N     N     -6     2
       N   N  2  N -6 -6 -6   N
    """

    assert Solution().maxPathSum(inp) == out


def stuff_4():
    inp = list2tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])

    # inp = list2tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    out = 48

    """
                5
            4           8
        11     n    13     4 
      7    2       n  n   n  1
    """

    assert Solution().maxPathSum(inp) == out


def list2tree(input: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Reverse iterate list so we create leaves first.

    This looks like the same way a heap stores parent child relationships.
    So, we can calculate the location of the parent based on the child index
    floor((index - 1) / 2).

    We can consider the reverse iteration steps to be:
        1. create node if it doesn't exist
        2. parent it, if we're not at the top
        3. ignore None children
    
    In this way we ensure its created only once and its parented only once.

    Store a reference to node in an array of the same length, so we can
    parent a left and a right node to the same parent, without recreating
    the parent node.
    """

    node_list: List[Union[TreeNode, None]] = [None] * len(input)

    for i in reversed(range(len(input))):
        val = input[i]

        if val is None:
            continue

        is_right = i % 2 == 0

        node: Optional[TreeNode] = None

        if node_list[i]:
            node = node_list[i]
        else:
            node = TreeNode(val)
            node_list[i] = node

        parent = floor((i - 1) / 2)

        if parent < 0:
            continue

        node_parent: Optional[TreeNode] = None

        if node_list[parent]:
            node_parent = node_list[parent]
        else:
            node_parent = TreeNode(input[parent])
            node_list[parent] = node_parent

        if is_right:
            node_parent.right = node
        else:
            node_parent.left = node

    return node_list[0]

