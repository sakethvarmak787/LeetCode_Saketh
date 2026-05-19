class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        left = 0

        ans = float('inf')

        bits = [0] * 32

        curr_or = 0

        for right in range(len(nums)):

            # add nums[right]
            for b in range(32):

                if nums[right] & (1 << b):

                    bits[b] += 1

                    curr_or |= (1 << b)

            # shrink window
            while left <= right and curr_or >= k:

                ans = min(ans, right - left + 1)

                # remove nums[left]
                for b in range(32):

                    if nums[left] & (1 << b):

                        bits[b] -= 1

                        # no number now contributes this bit
                        if bits[b] == 0:

                            curr_or ^= (1 << b)

                left += 1

        return ans if ans != float('inf') else -1