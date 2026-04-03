class Solution:
    def coinChange(self, coins, amount):
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0   # 0 coins needed for amount 0
        
        for x in range(1, amount + 1):
            for coin in coins:
                
                if x - coin >= 0:
                    dp[x] = min(dp[x], 1 + dp[x - coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1