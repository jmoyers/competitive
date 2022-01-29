"""Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""
from typing import List, Optional, Union
from math import floor


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This is not a BST, so our solution has to be purely from iteration
    order. This is going to be right sided dfs, where we keep track of
    the first value we see at a given depth.
    """

    def dfs(self, node: Optional[TreeNode], depth: int, result: List[int]) -> None:
        if len(result) == depth and node is not None:
            result.append(node.val)
        elif not node:
            return

        if node.right:
            self.dfs(node.right, depth + 1, result)
        if node.left:
            self.dfs(node.left, depth + 1, result)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        self.dfs(root, 0, result)
        return result


def test_1():
    assert Solution().rightSideView(list2tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]


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

