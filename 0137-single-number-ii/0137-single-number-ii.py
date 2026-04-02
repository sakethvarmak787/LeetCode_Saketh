class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0

        for i in range(32):
            bit_sum = 0

            for num in nums:
                if (num >> i) & 1:
                    bit_sum += 1

            if bit_sum % 3:
                res |= (1 << i)

        # Fix for negative numbers
        if res >= 2**31:
            res -= 2**32

        return res