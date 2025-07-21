class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        count = 1

        res.append(s[0])  

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1  
            
            if count < 3:
                res.append(s[i])  

        return ''.join(res)
