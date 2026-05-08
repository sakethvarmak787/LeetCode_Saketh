class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        for i in range(len(s)):
            for j in range(i,len(s)):
                sub = s[i:j+1]

                if sub == sub[::-1]:
                    res.append(sub)

        return len(res)
