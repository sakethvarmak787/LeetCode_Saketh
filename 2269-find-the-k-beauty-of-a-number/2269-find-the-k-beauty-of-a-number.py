class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        count = 0

        s = str(num)

        take = []

        for i in range(len(s) - k + 1):

            take.append(s[i:i+k])

        for arr in take:

            val = int(arr)

            if val != 0 and num % val == 0:

                count += 1

        return count