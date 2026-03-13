# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = []
        def dfs(node):
            if not node:
                return
            lst.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        mindiff = float('inf')

        for i in range(0,len(lst)):
            for j in range(i+1,len(lst)):
                mindiff = min(mindiff,abs(lst[i]-lst[j]))
            

        return mindiff
