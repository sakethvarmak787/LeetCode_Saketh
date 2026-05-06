class Solution:
    def check(self, nums: List[int]) -> bool:

        sorted_nums = sorted(nums)

        for i in range(len(nums)):

            nums2 = sorted_nums[i:] + sorted_nums[:i]

            if nums2 == nums:
                return True

        return False