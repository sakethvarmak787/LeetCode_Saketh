class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                curr_sub = s[i:j]
                if curr_sub == curr_sub[::-1]:
                    if len(curr_sub) > len(longest):
                        longest = curr_sub
        return longest