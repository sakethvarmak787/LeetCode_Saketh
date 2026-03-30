class Solution:
    def permute(self, nums):
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            # base case
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # choose
                path.append(nums[i])
                used[i] = True

                # explore
                backtrack(path)

               # undo (backtrack)
                path.pop()
                used[i] = False 

        backtrack([])
        return res