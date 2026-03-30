class Solution:
    def combine(self, n: int, k: int):
        res = []

        def backtrack(start, path):
            # base case
            if len(path) == k:
                res.append(path.copy())
                return

            # choices
            for i in range(start, n + 1):
                path.append(i)          # choose
                backtrack(i + 1, path) # explore
                path.pop()             # undo (backtrack)

        backtrack(1, [])
        return res