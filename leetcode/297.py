"""
---
title: Serialize and Deserialize Binary Tree
difficulty: hard
level: 3
tags:
- serialization
- binary tree
- deque
- codec
- compression
links: 
- https://leetcode.com/problems/serialize-and-deserialize-binary-tree
---
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes a
binary tree. You do not necessarily need to follow this format, so please be
creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your
serialize and deserialize algorithms should be stateless.
"""
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode):
        # we'll use breadth-first search to explore the tree and produce a
        # comma-seperated list. bfs uses a queue in its iterative form
        vals = []
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            if curr:
                vals.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                vals.append("*")

        return ",".join(vals)

    def deserialize(self, data: str):
        # this is a generator so we don't have to store the entire split
        # data in memory as a copy, just each individual item as processed
        vals = (int(val) if val != "*" else None for val in data.split(","))

        val = next(vals)

        if val is None:
            return None

        root = TreeNode(val)
        queue = deque([root])

        while queue:
            curr = queue.popleft()

            # may be no children, default None
            val = next(vals, None)

            if val != None:
                curr.left = TreeNode(val)
                # append to queue to process children, if present
                queue.append(curr.left)

            val = next(vals, None)

            if val != None:
                curr.right = TreeNode(val)
                queue.append(curr.right)

        return root


# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

codec = Codec()
codec.deserialize(codec.serialize(root))
