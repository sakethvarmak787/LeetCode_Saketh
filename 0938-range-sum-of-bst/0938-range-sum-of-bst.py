# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        def dfs(node):
            if not node:
                return None

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)

        new = []
        for i in range(len(res)):
            if res[i]>= low and res[i] <= high:
                new.append(res[i])

        return sum(new)
