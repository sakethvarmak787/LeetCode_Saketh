import math
from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        dictt = {}
        for pair in dimensions:
            i, j = pair
            res = math.sqrt(i*i + j*j)
            dictt[tuple(pair)] = res

       
        max_val = max(dictt.values())

     
        candidates = [pair for pair, val in dictt.items() if val == max_val]

       
        max_pair = max(candidates, key=lambda p: p[0] * p[1])
        prod = max_pair[0] * max_pair[1]

        return prod
