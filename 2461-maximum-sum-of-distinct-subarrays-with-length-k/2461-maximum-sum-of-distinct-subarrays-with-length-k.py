from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        freq = defaultdict(int)

        left = 0
        curr_sum = 0
        ans = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            freq[nums[right]] += 1

            if right - left + 1 > k:

                freq[nums[left]] -= 1
                curr_sum -= nums[left]

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            if right - left + 1 == k:
                if len(freq) == k:

                    ans = max(ans, curr_sum)

        return ans