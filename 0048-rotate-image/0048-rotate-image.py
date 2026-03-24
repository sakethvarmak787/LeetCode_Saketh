class Solution:
    def rotate(self, matrix):
        
        n = len(matrix)
        
        # STEP 1: transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # STEP 2: reverse each row
        for row in matrix:
            row.reverse()