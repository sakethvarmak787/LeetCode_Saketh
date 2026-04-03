class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n   # every element alone is length 1

        for i in range(n):
            for j in range(i):
                # if increasing
                if nums[i] > nums[j]:
                    # try extending
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)