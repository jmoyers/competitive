"""
Given a binary tree, you need to compute the length of the diameter of the
tree. The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of
edges between them.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_diameter = 0

    def dfs(self, node, depth=0) -> int:
        if not node or not node.left and not node.right:
            self.max_diameter = max(self.max_diameter, depth)
            return depth

        left, right = 0, 0

        if node.left:
            left = self.dfs(node.left, depth + 1)
        if node.right:
            right = self.dfs(node.right, depth + 1)

            # if the diameter of the tree passes through this node
            # and into both left and right child trees
        self.max_diameter = max((left - depth) + (right - depth), self.max_diameter)

        # return the max of either left or right
        return max(left, right)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_diameter


def test_lc1():
    inp = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    result = Solution().diameterOfBinaryTree(inp)
    assert result == 3
