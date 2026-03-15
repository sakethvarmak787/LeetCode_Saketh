class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])

            else:
                return nums[i]