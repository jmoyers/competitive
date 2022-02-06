# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = defaultdict(list)
        queue = deque()
        queue.append(root)
        queue.append(None)
        
        level = 1
        
        while len(queue) > 1:
            #print(list(n.val if n else None for n in queue))
            node = queue.popleft() 
            
            if not node:
                queue.append(None)
                level += 1
                continue
            
            ans[level].append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        
        return list(ans.values())
        
        
