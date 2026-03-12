# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def helper(node,path):
            if not node:
                return

            path.append(node.val)
            if not node.left and not node.right:
               res.append("->".join(map(str, path)))
            helper(node.left,path)
            helper(node.right,path)

            path.pop()

        helper(root,[])

        return res

        

            