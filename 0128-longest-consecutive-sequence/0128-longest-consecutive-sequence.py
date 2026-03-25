class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = sorted(set(nums))

        longest = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                curr_len += 1
            else:
                longest = max(longest, curr_len)
                curr_len = 1

        longest = max(longest, curr_len)
        return longest