# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return []
        
        res = []
        q = deque([root]) 

        while q:
            n = len(q)
            level = []
            
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
       
        sums = [sum(i) for i in res]
        max_index = sums.index(max(sums)) 
        return max_index + 1
        

        

