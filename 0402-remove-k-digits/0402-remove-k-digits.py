class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []  # this will store digits of final number
        
        # we go digit by digit
        for digit in num:
            
            # IMPORTANT IDEA:
            # while:
            # - we still have digits to remove (k > 0)
            # - AND stack is not empty
            # - AND last digit in stack is bigger than current digit
            # we remove that bigger digit
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()   # remove bigger digit
                k -= 1        # we used one removal
            
            # after fixing, we add current digit
            stack.append(digit)
            
            # ----------------------------------------
            # PARALLEL DRY RUN ("1432219", k=3)
            #
            # digit = '3'
            # stack = ['1','4']
            # 4 > 3 → pop → stack=['1'], k=2
            # now push 3 → stack=['1','3']
            #
            # digit = '2'
            # stack=['1','3']
            # 3 > 2 → pop → stack=['1'], k=1
            # push 2 → stack=['1','2']
            # ----------------------------------------
        
        # if we still have k left
        # means digits were increasing → remove from end
        while k > 0:
            stack.pop()
            k -= 1
        
        # build number
        result = "".join(stack)
        
        # remove leading zeros
        result = result.lstrip('0')
        
        # if empty, return "0"
        return result if result else "0"