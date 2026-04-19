from collections import deque

class Solution:
    def findBottomLeftValue(self, root):
        # We will use BFS (level order traversal)
        # Queue helps us process nodes level by level
        queue = deque([root])
        
        # This variable will store the leftmost value at each level
        leftmost_value = root.val
        
        # We continue until all nodes are processed
        while queue:
            
            # Number of nodes in current level
            level_size = len(queue)
            
            # Traverse all nodes in this level
            for i in range(level_size):
                
                # Pop node from front of queue
                node = queue.popleft()
                
                # VERY IMPORTANT:
                # If this is the first node in this level,
                # then it is the LEFTMOST node
                if i == 0:
                    leftmost_value = node.val
                
                # Add left child first
                # (this ensures leftmost comes first in next level)
                if node.left:
                    queue.append(node.left)
                
                # Add right child
                if node.right:
                    queue.append(node.right)
        
        
        return leftmost_value