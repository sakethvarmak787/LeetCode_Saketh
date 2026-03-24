class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        map_p = {}
        map_s = {}
        
        for i in range(len(pattern)):
            c1 = pattern[i]
            c2 = words[i]   
            
            if c1 in map_p:
                if map_p[c1] != c2:
                    return False
            else:
                map_p[c1] = c2
            
            if c2 in map_s:
                if map_s[c2] != c1:
                    return False
            else:
                map_s[c2] = c1
        
        return True