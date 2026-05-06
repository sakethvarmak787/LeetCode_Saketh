class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])

        for r in range(ROWS - 1, -1, -1):
            for c1 in range(COLS - 1, -1, -1):
                if boxGrid[r][c1] == '#':
                    c2 = c1 + 1
                    while c2 < COLS and boxGrid[r][c2] == '.':
                        c2 += 1

                    boxGrid[r][c1] = '.'
                    boxGrid[r][c2 - 1] = '#'


        res = []
        for c in range(COLS):
            col = []
            for r in range(ROWS - 1, -1, -1):
                col.append(boxGrid[r][c])
            res.append(col)
        return res


