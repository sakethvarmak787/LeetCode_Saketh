class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            curr_min = nums[i]
            curr_max = nums[i]

            for j in range(i, len(nums)):
                curr_min = min(curr_min, nums[j])
                curr_max = max(curr_max, nums[j])

                result += curr_max - curr_min

        return result