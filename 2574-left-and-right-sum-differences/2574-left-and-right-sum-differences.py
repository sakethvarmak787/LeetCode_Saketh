class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left = []
        total = 0

        for num in nums:

            left.append(total)

            total += num

        right = [0] * len(nums)

        total = 0

        for i in range(len(nums)-1,-1,-1):

            right[i] = total

            total += nums[i]

        res = []

        for i in range(len(nums)):

            res.append(abs(left[i] - right[i]))

        return res