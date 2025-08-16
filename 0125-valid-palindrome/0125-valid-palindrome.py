class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(ch.lower() for ch in s if ch.isalnum())
        return ss == ss[::-1]
