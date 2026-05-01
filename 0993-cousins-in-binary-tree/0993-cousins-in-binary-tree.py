from collections import deque

class Solution:
    def isCousins(self, root, x, y):
        queue = deque([(root, 0, None)]) 
        
        x_info = None
        y_info = None
        
        while queue:
            node, depth, parent = queue.popleft()
            
            if node.val == x:
                x_info = (depth, parent)
            
            if node.val == y:
                y_info = (depth, parent)
            
            if x_info and y_info:
                break
            
            if node.left:
                queue.append((node.left, depth + 1, node))
            
            if node.right:
                queue.append((node.right, depth + 1, node))
        

        x_depth, x_parent = x_info
        y_depth, y_parent = y_info
        
        return (x_depth == y_depth) and (x_parent != y_parent)