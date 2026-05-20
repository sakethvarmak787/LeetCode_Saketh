from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        seen = defaultdict(int)

        # remainder 0 already exists once
        seen[0] = 1

        total = 0
        count = 0

        for num in nums:

            total += num

            rem = total % k

            # same remainder seen before
            count += seen[rem]

            # store remainder
            seen[rem] += 1

        return count