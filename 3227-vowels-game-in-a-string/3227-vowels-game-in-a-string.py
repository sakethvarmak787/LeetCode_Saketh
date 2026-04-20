class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        vowels = set("aeiou")
        vowel_count = 0
        
        for ch in s:
            if ch in vowels:
                vowel_count += 1
        
        if vowel_count == 0:
            return False
    
        return True


