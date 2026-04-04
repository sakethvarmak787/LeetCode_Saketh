class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)

        # dp[i][j] = min operations to convert word1[i:] → word2[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base cases
        for j in range(n + 1):
            dp[m][j] = n - j   # insert remaining chars : word1 finished

        for i in range(m + 1):
            dp[i][n] = m - i   # delete remaining chars: word2 finished

        # fill from bottom-right → top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert = dp[i][j + 1]
                    delete = dp[i + 1][j]
                    replace = dp[i + 1][j + 1]

                    dp[i][j] = 1 + min(insert, delete, replace)

        return dp[0][0]