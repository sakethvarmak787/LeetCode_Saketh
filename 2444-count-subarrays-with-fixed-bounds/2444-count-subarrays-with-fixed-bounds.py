class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        last_min = -1
        last_max = -1
        last_invalid = -1

        count = 0

        for i in range(len(nums)):

            # invalid number
            if nums[i] < minK or nums[i] > maxK:
                last_invalid = i

            # found minK
            if nums[i] == minK:
                last_min = i

            # found maxK
            if nums[i] == maxK:
                last_max = i

            count += max(
                0,
                min(last_min, last_max) - last_invalid
            )

        return count