from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        new = []
        a,b= edges[0]
        c,d = edges[1]
        if c==a or d==a:
            return a

        elif c==b or d==b:
            return b

        else:
            return -1
            

                