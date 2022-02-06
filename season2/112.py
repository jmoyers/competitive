# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, targetSum):
        if not node:
            return False

        if node.left or node.right:
            return self.dfs(node.left, targetSum - node.val) or self.dfs(
                node.right, targetSum - node.val
            )
        else:
            return targetSum - node.val == 0

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.dfs(root, targetSum)
