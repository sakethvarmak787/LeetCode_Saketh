class Solution:
    def maxProfit(self,prices):
        n = len(prices)

    # dp[i][canBuy][k]
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

    # fill from back
        for i in range(n - 1, -1, -1):
            for canBuy in range(2):
                for k in range(1, 3):

                    if canBuy:
                        buy = -prices[i] + dp[i + 1][0][k]
                        skip = dp[i + 1][1][k]
                        dp[i][1][k] = max(buy, skip)
                    else:
                        sell = prices[i] + dp[i + 1][1][k - 1]
                        skip = dp[i + 1][0][k]
                        dp[i][0][k] = max(sell, skip)

        return dp[0][1][2]