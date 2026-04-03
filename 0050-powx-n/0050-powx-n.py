class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            result = 1
            
            while n > 0:         #We square the base and halve the power
                if n % 2 == 1:   #“If power is even → square the base
                               #If power is odd → take one x and continue”
                    result *= x
                
                x *= x
                n //= 2
            
            return result
        
        # handle negative power
        if n < 0:
            x = 1 / x
            n = -n
        
        return fastPow(x, n)