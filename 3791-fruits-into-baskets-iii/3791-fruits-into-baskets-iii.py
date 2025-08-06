from typing import List
from math import sqrt

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        group = int(sqrt(n))
        groups_count = (n + group) // group
        groups = [0] * groups_count

       
        for i in range(n):
            groups[i // group] = max(groups[i // group], baskets[i])

        res = 0
        for fruit in fruits:
            used = False
            for i in range(groups_count):
                if groups[i] < fruit:
                    continue
                groups[i] = 0
                pos = i * group
                for j in range(pos, min(n, pos + group)):
                    if baskets[j] >= fruit and not used:
                        baskets[j] = 0 
                        used = True
                    else:
                        groups[i] = max(groups[i], baskets[j])
                if used:
                    break
            if not used:
                res += 1

        return res
