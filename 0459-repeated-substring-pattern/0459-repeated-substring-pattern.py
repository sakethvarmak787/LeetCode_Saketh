class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        combined = s + s
        
        cut = combined[1:-1]
        
        if s in cut:
            return True
            
        return False