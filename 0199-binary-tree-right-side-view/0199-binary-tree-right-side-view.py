from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                
               
                if i == level_length - 1:
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res
