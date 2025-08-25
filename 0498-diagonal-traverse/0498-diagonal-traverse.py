from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m = len(mat)
        n = len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1 

        while len(result) < m * n:
            result.append(mat[row][col])

            if direction == 1:
                
                new_row, new_col = row - 1, col + 1

                if new_row < 0 or new_col >= n:
                   
                    direction = -1
                    if new_col >= n:
                       
                        row += 1
                    else:
                       
                        col += 1
                else:
                    row, col = new_row, new_col
            else: 
               
                new_row, new_col = row + 1, col - 1

                if new_row >= m or new_col < 0:
                   
                    direction = 1
                    if new_row >= m:
                       
                        col += 1
                    else:
                       
                        row += 1
                else:
                    row, col = new_row, new_col

        return result