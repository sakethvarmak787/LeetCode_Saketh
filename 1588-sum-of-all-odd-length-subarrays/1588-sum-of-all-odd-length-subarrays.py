class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        prefix = [0]

        total = 0

        for num in arr:

            total += num

            prefix.append(total)

        ans = 0

        for left in range(len(arr)):

            for right in range(left, len(arr)):

                length = right - left + 1

                if length % 2 == 1:

                    sub_sum = prefix[right+1] - prefix[left]

                    ans += sub_sum

        return ans