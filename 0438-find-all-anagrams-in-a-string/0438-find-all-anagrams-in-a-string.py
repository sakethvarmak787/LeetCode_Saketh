class Solution:
    def findAnagrams(self, s: str, p: str):
        result = []
        k = len(p)
        sorted_p = sorted(p)
    
        for i in range(len(s) - k + 1):
            substring = s[i:i + k]
            sorted_sub = sorted(substring)
            if sorted_sub == sorted_p:
                result.append(i)
                
        return result