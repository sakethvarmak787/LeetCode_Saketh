# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        resp = []
        resq = []

        def preorder(node,res):
            if not node:
                res.append(None)
                return
            res.append(node.val)
            preorder(node.left,res)
            preorder(node.right,res)

        preorder(p,resp)
        preorder(q,resq)

        return resp == resq

    



        

        
        