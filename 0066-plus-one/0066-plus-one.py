class Solution:
    def plusOne(self, digits):
        res = 0
        
        # build number
        for i in range(len(digits)):
            res = (res * 10) + digits[i]
        
        # add 1
        res += 1
        
        # convert back to list
        return [int(x) for x in str(res)]