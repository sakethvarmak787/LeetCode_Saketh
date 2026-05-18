class Solution:
    def atMost(self, nums, goal):

        if goal < 0:
            return 0

        left = 0
        total = 0
        count = 0

        for right in range(len(nums)):

            total += nums[right]

            while total > goal:

                total -= nums[left]
                left += 1

            count += (right - left + 1)

        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)