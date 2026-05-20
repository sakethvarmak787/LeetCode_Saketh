class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        seen = {0: -1}

        total = 0
        ans = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                total += 1
            else:
                total -= 1
            if total in seen:

                ans = max(ans, i - seen[total])

            else:
                seen[total] = i

        return ans