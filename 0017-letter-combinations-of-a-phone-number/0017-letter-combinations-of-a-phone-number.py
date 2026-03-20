class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""]   

        for digit in digits:
            letters = mapping[digit]
            new_res = []

            for word in res:
                for letter in letters:
                    new_res.append(word + letter)

            res = new_res

        return res