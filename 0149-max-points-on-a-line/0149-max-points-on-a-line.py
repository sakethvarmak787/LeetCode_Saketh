from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 1. For each point, check how many points lie on same line
        # 2. Count points with same slope
        # 3. Update result with max

        n = len(points)
        if n <= 2:
            return n

        res = 1

        for i in range(n):
            p1 = points[i]
            count = defaultdict(int)

            for j in range(i + 1, n):
                p2 = points[j]

                if p2[0] == p1[0]:       #if points on same line, we get to didvide by 0, because (x2-x1), the denominator becomes zero, so we set slope to be inf
                    slope = float("inf")   # vertical line
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                count[slope] += 1
                res = max(res, count[slope] + 1)

        return res