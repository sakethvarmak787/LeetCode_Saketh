class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        nums.sort()

        count = 0

        l = 0
        r = len(nums) - 1

        while l < r:

            total = nums[l] + nums[r]

            if total < target:

                count += (r - l)

                l += 1

            else:

                r -= 1

        return count