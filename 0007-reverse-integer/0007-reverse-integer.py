class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        revnum = 0
        while x > 0:
            ld = x % 10
            x //= 10
            revnum = (revnum * 10) + ld
        
        revnum *= sign
        
        if revnum < INT_MIN or revnum > INT_MAX:
            return 0
        return revnum
