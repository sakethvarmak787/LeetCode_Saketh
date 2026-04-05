class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)

        dp = [[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for canBuy in range(2):
                for t in range(1, k+1):

                    if canBuy:
                        buy = -prices[i] + dp[i+1][0][t]
                        skip = dp[i+1][1][t]
                        dp[i][1][t] = max(buy, skip)
                    else:
                        sell = prices[i] + dp[i+1][1][t-1]
                        skip = dp[i+1][0][t]
                        dp[i][0][t] = max(sell, skip)

        return dp[0][1][k]