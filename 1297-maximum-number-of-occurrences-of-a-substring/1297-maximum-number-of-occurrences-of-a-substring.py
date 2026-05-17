class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        seen = defaultdict(int)

        freq = defaultdict(int)

        left = 0

        ans = 0

        for right in range(len(s)):

            # add current char
            seen[s[right]] += 1

            # keep window size = minSize
            if right - left + 1 > minSize:

                seen[s[left]] -= 1

                if seen[s[left]] == 0:
                    del seen[s[left]]

                left += 1

            # valid window
            if (
                right - left + 1 == minSize and
                len(seen) <= maxLetters
            ):

                sub = s[left:right + 1]

                freq[sub] += 1

                ans = max(ans, freq[sub])

        return ans