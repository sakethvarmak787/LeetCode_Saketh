class Solution:
    def hammingWeight(self, n: int) -> int:
        counts = 0

        while n:
            counts += n & 1
            n >>= 1

        return counts