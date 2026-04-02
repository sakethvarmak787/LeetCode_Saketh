class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        
        # Step 1: keep shifting both until they become equal
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Step 2: shift back to restore common prefix
        return left << shift