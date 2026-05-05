from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        new = []
        for sub in edges:
            for val in sub:
                new.append(val)

        dictt = Counter(new)
        ans = max(dictt, key=dictt.get)
        return ans
