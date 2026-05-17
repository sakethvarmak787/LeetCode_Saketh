class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        
        left = 0
        maxf = 0
        longest = 0

        for right in range(len(s)):

            # add current character
            count[s[right]] = 1 + count.get(s[right], 0)

            # maximum frequency character in window
            maxf = max(maxf, count[s[right]])

            # if replacements needed > k
            while (right - left + 1) - maxf > k:

                count[s[left]] -= 1
                left += 1

            # update answer
            longest = max(longest, right - left + 1)

        return longest