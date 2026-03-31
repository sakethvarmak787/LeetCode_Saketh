# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        
        def build(r, c, size):
            # STEP 1: check if all values are same
            first = grid[r][c]
            is_same = True
            
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        is_same = False
                        break
                if not is_same:
                    break
            
            # STEP 2: if uniform → leaf node
            if is_same:
                return Node(first == 1, True)
            
            # STEP 3: otherwise split into 4 parts
            half = size // 2
            
            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)
            
            # STEP 4: create internal node
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return build(0, 0, len(grid))