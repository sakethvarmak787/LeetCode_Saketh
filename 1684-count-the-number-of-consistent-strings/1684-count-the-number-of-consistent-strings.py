class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = 0

        for word in words:

            if set(word) <= set(allowed):
                count += 1

        return count