# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

class Solution:
    def __init__(self):
        self.visited = set()
        
    def distanceK(self, root: 'TreeNode', target: 'TreeNode', K: int) -> List[int]:
        self.attach_parent(root, None)
        results = []
        self._distanceK(target, K, results)
        return results
    
    def attach_parent(self, node, parent):
        if not node:
            return
        
        node.parent = parent
        self.attach_parent(node.left, node)
        self.attach_parent(node.right, node)        
    
    def _distanceK(self, node, k, results = []):
        if node is None:
            return
        
        if node.val in self.visited:
            return
        
        self.visited.add(node.val)        
        
        if k == 0:
            results.append(node.val)
            return
        
        self._distanceK(node.parent, k - 1, results)
        self._distanceK(node.left, k - 1, results)
        self._distanceK(node.right, k - 1, results)
