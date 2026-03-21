class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        nums = [1,2,3,4,5,6,7,8,9]

        def backtrack(start, path, total):
            if total > n:
                return
            if len(path) == k:
                if total == n:
                    res.append(path[:])   
                return
            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(i + 1, path, total + nums[i])

                path.pop() 

        backtrack(0, [], 0)
        return res