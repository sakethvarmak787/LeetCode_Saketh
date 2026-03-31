class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()       # columns
        diag1 = set()      # r - c
        diag2 = set()      # r + c

        res = 0

        def backtrack(row):
            nonlocal res

            # base case
            if row == n:
                res += 1
                return

            for col in range(n):
                # check if safe
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # remove queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res