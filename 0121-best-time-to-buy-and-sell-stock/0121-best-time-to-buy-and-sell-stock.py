class Solution:
    def maxProfit(self, prices):
        maxprofit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i] - min_price)

        return maxprofit

        #updating minimum buy so far, and compare with current price