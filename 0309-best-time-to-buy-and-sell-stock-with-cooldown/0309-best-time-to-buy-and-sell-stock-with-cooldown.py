class Solution:
    def maxProfit(self, prices):
        
        n = len(prices)
    
        
        hold = -prices[0]
        sold = 0
        rest = 0
        
        for i in range(1, n):
            
            new_hold = max(hold, rest - prices[i])
            
            new_sold = hold + prices[i]
            
            new_rest = max(rest, sold)
            
            hold = new_hold
            sold = new_sold
            rest = new_rest
        
        return max(sold, rest)