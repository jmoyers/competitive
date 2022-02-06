# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, k):
        if not node or self.k == k:
            return
        
        self.inorder(node.left, k)
        
        self.k += 1
        if k == self.k:
            self.k_val = node.val
        
        self.inorder(node.right, k)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order traversal gives a sorted array ascended
        self.k = 0
        self.inorder(root, k)
        return self.k_val
        
