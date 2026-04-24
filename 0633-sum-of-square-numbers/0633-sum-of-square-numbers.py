class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c ** 0.5)  # largest possible b

        while a <= b:
            curr = a*a + b*b

            if curr == c:
                return True
            elif curr < c:
                a += 1   # need bigger sum
            else:
                b -= 1   # need smaller sum

        return False