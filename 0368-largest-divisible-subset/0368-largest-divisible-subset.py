class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}  # (i, prevIndex) -> List

        def dfs(i, prevIndex):
            if i == len(nums):
                return []
            if (i, prevIndex) in cache:
                return cache[(i, prevIndex)]

            res = dfs(i + 1, prevIndex)  # Skip nums[i]
            if prevIndex == -1 or nums[i] % nums[prevIndex] == 0:
                tmp = [nums[i]] + dfs(i + 1, i)  # Include nums[i]
                res = tmp if len(tmp) > len(res) else res

            cache[(i, prevIndex)] = res
            return res

        return dfs(0, -1)