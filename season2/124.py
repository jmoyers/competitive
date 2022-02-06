# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        at_node_max = max(node.val + left + right,  node.val + left, node.val + right, node.val)
        
        self.max = max(at_node_max, self.max)
        
        return max(node.val, node.val + left, node.val + right)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # any node as root
        # max of left
        # max of right
        # max(max(left, right) + node.val, self.ans)
        self.max = -math.inf
        self.dfs(root)
        return self.max
        
