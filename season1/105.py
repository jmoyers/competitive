"""
---
number: 105
title: Construct Binary Tree from Preorder and Inorder Traversal
difficulty: medium
---
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        preorder primarily gives us the root at a given level
        we iterate through the preorder list as the basis for processing
        the inorder list can be used to split the remaining nodes into left and right
        subtrees. the reason for this is that the inorder traversal goes left, root, right.
        so, if we have the root from the preorder traversal, then we can partition the list
        by left and right subtrees.
        
        so, next choice is how to model the problem. if we know the root, it becomes convenient
        to process the list from the root down at each level. then its somewhat like a normal
        dfs, so we can use recursion to model the problem.
        
        further, to stop us from having to do a linear search to find the value of the new root
        inside the inorder traversal so we can parition list, we can build a hash map from
        the list. this lets us get O(1) lookup to find the parition for the
        recursive calls
        
        The real takeaway here is to know what inorder vs preorder vs postorder
        vs bfs means with regards to traversal order and to realize the naming
        convention for these traversal orders is based on a binary search tree.
        "in order" means nothing if the values don't actually end up in order or
        non-decreasing, at least.

        inorder = left, root, right -- starts at left leaf
        preorder (normally how i write a dfs) = 
            root, left, right OR top -> bottom, left -> right
        post-order = bottom -> top, left -> right
        bfs = top -> bottom, left -> right
        """

        # we use this to linearly process the nodes, paritioning by the root found
        # at the preorder index as we traverse the tree via dfs
        self.preorder_index = 0
        self.preorder = preorder

        # we'll make the inorder list a hash map, so that we can look up the location
        # based on the value provided to us as we do the preorder linear processing
        self.inorder = {key: val for val, key in enumerate(inorder)}

        return self.helper(0, len(preorder))

    def helper(self, start, end):
        if start == end:
            return None

        val = self.preorder[self.preorder_index]
        root = TreeNode(val)

        self.preorder_index += 1

        # index by which we are splitting the tree left/root/right, e.g. inorder traversal
        # parition is the index of the root of either the tree or a subtree, and is also
        # the node for the value that we're processing at this stage of the recursion
        partition = self.inorder[val]

        # it may not actually have children, if the start == parition or start + 1 == end,
        # then it has no nodes. we're handling that through the case case above
        root.left = self.helper(start, partition)
        root.right = self.helper(partition + 1, end)

        return root
