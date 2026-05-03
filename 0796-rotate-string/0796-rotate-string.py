class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        result = []

        for i in range(len(s)):
            new_str = s[i:] + s[:i]
            result.append(new_str)

        if goal in result:
            return True
        else:
            return False
