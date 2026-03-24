class Solution:
    def isValidSudoku(self, board):
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                
                val = board[r][c]
                
                if val == ".":
                    continue
                
                # calculate box index
                box = (r // 3) * 3 + (c // 3)
                
                # check duplicates
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False
                
                # add value
                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)
        
        return True