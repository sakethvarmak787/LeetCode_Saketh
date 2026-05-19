class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix = [0]

        total = 0

        for num in nums:

            total += num

            prefix.append(total)

        res = []

        for i in range(n):

            left_sum = prefix[i]

            right_sum = prefix[n] - prefix[i+1]

            left = nums[i] * i - left_sum

            right = right_sum - nums[i] * (n-i-1)

            res.append(left + right)

        return res