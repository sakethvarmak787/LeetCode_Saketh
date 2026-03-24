class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_flag = False
        col_flag = False

        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: mark using first row & column
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        row_flag = True
                    if c == 0:
                        col_flag = True
                    if r != 0 and c != 0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0

        # Step 2: fill based on markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 3: update first row
        if row_flag:
            for c in range(cols):
                matrix[0][c] = 0

        # Step 4: update first column
        if col_flag:
            for r in range(rows):
                matrix[r][0] = 0