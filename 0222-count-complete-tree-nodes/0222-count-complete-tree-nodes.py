class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def lefttree(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def righttree(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        height1 = lefttree(root)
        height2 = righttree(root)

        
        if height1 == height2:
            return (2 ** height1) - 1

        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)