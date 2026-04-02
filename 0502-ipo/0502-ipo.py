import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, 
                             profits: List[int], capital: List[int]) -> int:
        
        maxProfit = []  # max heap (store profits)
        
        # min heap based on capital required
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for _ in range(k):

            # add all projects we can afford
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1*p)  # max heap using negative

            # if no projects available
            if not maxProfit:
                break

            # take the project with max profit
            w += -1* heapq.heappop(maxProfit)

        return w