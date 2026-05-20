from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        seen = defaultdict(int)

        # prefix sum 0 seen once
        seen[0] = 1

        curr_sum = 0
        count = 0

        for num in nums:

            curr_sum += num

            # check if curr_sum - k already existed
            count += seen[curr_sum - k]

            # store current prefix sum
            seen[curr_sum] += 1

        return count