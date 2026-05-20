class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        seen = {0: -1}

        total = 0

        for i in range(len(nums)):

            total += nums[i]

            rem = total % k
            if rem in seen:

                if i - seen[rem] >= 2:
                    return True

            else:
                seen[rem] = i

        return False