class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        prefix = [0]

        total = 0

        for num in nums:

            total += num

            prefix.append(total)

        least = min(prefix)

        return 1 - least