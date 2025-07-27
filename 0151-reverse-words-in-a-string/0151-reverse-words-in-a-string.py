class Solution:
    def reverseWords(self, s: str) -> str:
        new = s.split()
        rev = new[::-1]
        res = ' '.join(rev)
        return res