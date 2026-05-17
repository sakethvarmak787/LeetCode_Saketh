class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        ans = ""
        for l in range(len(s)):

            for r in range(l, len(s)):
                sub = s[l:r+1]
                st = set(sub)
                nice = True
                for ch in sub:
                    if ch.lower() not in st or ch.upper() not in st:

                        nice = False
                        break

                if nice and len(sub) > len(ans):
                    ans = sub

        return ans