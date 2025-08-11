class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7

      
        powers = []
        power_of_2 = 1
        while n > 0:
            if n & 1 == 1:
                powers.append(power_of_2)
            power_of_2 *= 2
            n >>= 1
        
       
        prefix_products = [1] * (len(powers) + 1)
        for i in range(len(powers)):
            prefix_products[i + 1] = (prefix_products[i] * powers[i]) % MOD
        
        answers = []
        for left, right in queries:
            
            numerator = prefix_products[right + 1]
            denominator_inverse = pow(prefix_products[left], MOD - 2, MOD)
            
            answer = (numerator * denominator_inverse) % MOD
            answers.append(answer)
            
        return answers