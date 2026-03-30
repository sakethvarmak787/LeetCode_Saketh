class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(index, path):
            # base case: full combination formed
            if index == len(digits):
                res.append(path)
                return

            # get letters for current digit
            letters = mapping[digits[index]]

            for letter in letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return res