# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def build(self, node, output):
        if not node:
            output.append("X")
            return
        
        output.append(str(node.val))
        self.build(node.left, output)
        self.build(node.right, output)
        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = []
        self.build(root, output)
        return ",".join(output)
        
    def dfs(self, inp):
        val = next(inp)
        
        if val == "X":
            return None
        
        node = TreeNode(int(val))
        node.left = self.dfs(inp)
        node.right = self.dfs(inp)
        return node
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        inp = iter(data.split(','))
        return self.dfs(inp)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
