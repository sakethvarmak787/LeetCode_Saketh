class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, currsum):
            # base case
            if currsum == target:
                res.append(path.copy())
                return

            if currsum > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])                   # choose
                backtrack(i, path, currsum + candidates[i]) # reuse allowed
                path.pop()                                  # undo

        backtrack(0, [], 0)
        return res