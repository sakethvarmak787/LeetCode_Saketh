"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # If the root is null, there are no levels to process.
        # Return an empty list immediately to handle the edge case.
        if not root:
            return []
        
        result = []
        # We use a deque (double-ended queue) for efficient O(1) pops from the left.
        # Start by placing the root node in the queue to begin the BFS.
        queue = deque([root])
        
        while queue:
            # At the start of this loop, the queue contains ONLY nodes 
            # belonging to the current level we are about to process.
            level_size = len(queue)
            current_level_values = []
            
            # We must process exactly 'level_size' nodes to stay within this level.
            for _ in range(level_size):
                # Remove the oldest node from the front of the queue.
                node = queue.popleft()
                
                # Add this node's value to the list representing the current level.
                current_level_values.append(node.val)
                
                # Since this is an n-ary tree, 'node.children' is a list.
                # We add all children to the back of the queue. 
                # They will wait until the next level iteration to be processed.
                if node.children:
                    for child in node.children:
                        queue.append(child)
            
            # Once the inner loop finishes, the level is complete.
            # We append the group of values to our final results list.
            result.append(current_level_values)
            
        return result