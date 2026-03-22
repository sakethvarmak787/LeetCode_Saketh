class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words =s.split()

        n = len(words)
        last = words[n-1]

        return len(last)