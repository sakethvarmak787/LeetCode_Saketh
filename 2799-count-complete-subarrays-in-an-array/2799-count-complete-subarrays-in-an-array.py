class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        left = 0
        count = 0

        total_distinct = len(set(nums))

        freq = {}

        for right in range(len(nums)):

            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while len(freq) == total_distinct:

                count += (len(nums) - right)

                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

        return count