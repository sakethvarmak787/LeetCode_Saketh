class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        # every single char is palindrome
        for i in range(n):
            dp[i][i] = True

        # fill table
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):

                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        if (j - i + 1) > max_len:
                            start = i
                            max_len = j - i + 1

        return s[start:start + max_len]