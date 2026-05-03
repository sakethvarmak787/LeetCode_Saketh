class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        
        # store last position of each digit
        last = {int(d): i for i, d in enumerate(digits)}
        
        for i, d in enumerate(digits):
            for bigger in range(9, int(d), -1):
                if bigger in last and last[bigger] > i:
                    # swap
                    j = last[bigger]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))
        
        return num