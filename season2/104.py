# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, curr_level):
        left, right = curr_level, curr_level

        if node.left:
            left = self.dfs(node.left, curr_level + 1)
        if node.right:
            right = self.dfs(node.right, curr_level + 1)

        return max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.dfs(root, 1)
