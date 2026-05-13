class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ss = Counter(s)
        for ch in t:
            if ch in ss and ss[ch]>0:
                ss[ch] -= 1

        return sum(ss.values())


