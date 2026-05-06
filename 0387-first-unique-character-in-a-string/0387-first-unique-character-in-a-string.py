class Solution:
    def firstUniqChar(self, s: str) -> int:
        ss = Counter(s)
        for i,ch in enumerate(s):
            if ss[ch] == 1:
                return i
        
        return -1