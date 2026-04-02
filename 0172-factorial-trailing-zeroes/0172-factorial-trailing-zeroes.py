class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        
        while n > 0:
            n //= 5 #trailing zeroes comes from mostly 2,but few 5's . so take 5
            count += n
        
        return count