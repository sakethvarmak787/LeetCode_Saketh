class Solution:
    def findRepeatedDnaSequences(self, s: str):

        if len(s) < 10:
            return []
        seen = set()
        added = set()
        k = 10

        for i in range(len(s) - k + 1):

            window = s[i:i+k]

            if window in seen:
                added.add(window)
            else:
                seen.add(window)

        return list(added)