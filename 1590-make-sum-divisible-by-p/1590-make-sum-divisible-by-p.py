class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        total = sum(nums)

        rem = total % p
        if rem == 0:
            return 0

        seen = {0: -1}

        prefix = 0

        ans = len(nums)

        for i in range(len(nums)):

            prefix += nums[i]

            curr_rem = prefix % p

            need = (curr_rem - rem) % p

            if need in seen:

                ans = min(ans, i - seen[need])

            seen[curr_rem] = i

        return ans if ans < len(nums) else -1