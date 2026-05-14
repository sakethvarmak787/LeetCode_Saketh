class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums.sort()
        l = 0
        r = 1
        count = 0

        while r < len(nums):
            if l == r:
                r += 1
                continue

            diff = nums[r] - nums[l]

            if diff == k:

                count += 1

                l += 1
                r += 1
                while r < len(nums) and nums[r] == nums[r-1]:
                    r += 1

            elif diff < k:
                r += 1

            else:
                l += 1

        return count