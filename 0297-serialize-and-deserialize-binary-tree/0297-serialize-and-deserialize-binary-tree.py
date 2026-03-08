# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []
        
        def dfs(node):
            if not node:
                # We need to record nulls to preserve the tree structure
                res.append("null")
                return
            
            # Pre-order: Root, then Left, then Right
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        # Split the string back into individual node values
        vals = data.split(",")
        # Use an iterator or index to keep track of our position in the list
        self.cursor = 0
        
        def dfs():
            if self.cursor >= len(vals):
                return None
            
            val = vals[self.cursor]
            self.cursor += 1
            
            if val == "null":
                return None
            
            # Create the node and recursively build its children
            # The order must match the serialization order (Root -> Left -> Right)
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            
            return node
            
        return dfs()