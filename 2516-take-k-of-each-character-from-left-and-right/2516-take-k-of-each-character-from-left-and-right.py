from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        if total['a'] < k or total['b'] < k or total['c'] < k:
            return -1

        l = 0
        longest = 0
        window = {
            'a': 0,
            'b': 0,
            'c': 0
        }

        for r in range(len(s)):
            window[s[r]] += 1

            while (
                window['a'] > total['a'] - k or
                window['b'] > total['b'] - k or
                window['c'] > total['c'] - k
            ):

                window[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return len(s) - longest