from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        longest = 0

        for i in range(len(s)):

            ss = defaultdict(int)

            for j in range(i, len(s)):

                ss[s[j]] += 1

                valid = True

                # check all frequencies
                for val in ss.values():

                    if val < k:
                        valid = False
                        break

                if valid:
                    longest = max(longest, j - i + 1)

        return longest