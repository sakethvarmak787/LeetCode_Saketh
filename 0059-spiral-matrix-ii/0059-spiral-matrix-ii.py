class Solution:
    def generateMatrix(self, n: int):
        
        # Create empty matrix
        matrix = [[0] * n for _ in range(n)]
        
        # Boundaries of current layer
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        
        # Start filling from 1
        num = 1
        
        # Keep filling until all numbers are placed
        while top <= bottom and left <= right:
            
            # 1. Fill top row (left → right)
            # WHY? → This is the top edge of current box
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
                
                # Dry run (n=3):
                # matrix[0][0]=1, matrix[0][1]=2, matrix[0][2]=3
            
            # Top row is now used → move boundary down
            top += 1
            
            # 2. Fill right column (top → bottom)
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
                
                # matrix[1][2]=4, matrix[2][2]=5
            
            # Right column is used → move boundary left
            right -= 1
            
            # 3. Fill bottom row (right → left)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                    
                    # matrix[2][1]=6, matrix[2][0]=7
                
                bottom -= 1
            
            # 4. Fill left column (bottom → top)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                    
                    # matrix[1][0]=8
                
                left += 1
        
        return matrix