from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        total_squares = 0
        max_side = min(m, n)
        
        for side in range(1, max_side + 1):
            for row in range(m - side + 1):
                for col in range(n - side + 1):
                    is_all_ones = True
                    
                    for i in range(side):
                        for j in range(side):
                            if matrix[row + i][col + j] == 0:
                                is_all_ones = False
                                break  
                        if not is_all_ones:
                            break 
                    
                    if is_all_ones:
                        total_squares += 1
        
        return total_squares