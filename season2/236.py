# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root == p or root == q:
            return root

        # p or q is left is left is true
        left = self.lowestCommonAncestor(root.left, p, q)

        # p or q is right if right is true
        right = self.lowestCommonAncestor(root.right, p, q)

        # this is lca
        if left and right:
            return root

        # p and q are not in left, must both be right
        if not left:
            return right

        if not right:
            return left

