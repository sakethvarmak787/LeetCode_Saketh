class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        total = sum(nums)

        find = total - x

        if find < 0:
            return -1

        if find == 0:
            return len(nums)

        left = 0

        maxx = -1

        add = 0

        for right in range(len(nums)):

            add += nums[right]

            while add > find:

                add -= nums[left]
                left += 1

            if add == find:

                maxx = max(
                    maxx,
                    right - left + 1
                )

        if maxx == -1:
            return -1

        return len(nums) - maxx