# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        queue.append(None)
        
        level = 1
        
        ans = defaultdict(list)
        
        while queue:
            #print(list(n.val if n else None for n in queue))
            
            node = queue.popleft()
            
            if not node:
                if level % 2 == 0:
                    ans[level].reverse()
                level += 1
                if queue:
                    queue.append(None)
                continue
            
            ans[level].append(node.val)
                
            if node.left:
                queue.append(node.left) 
            if node.right:
                queue.append(node.right) 
                
        return list(ans.values())
