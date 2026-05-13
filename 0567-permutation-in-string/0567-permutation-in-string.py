class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1
        
        window_count = {}
        left = 0
    
        for right in range(len(s2)):
            ch = s2[right]
            window_count[ch] = window_count.get(ch, 0) + 1
            
            if right - left + 1 > len(s1):
                left_char = s2[left]
                window_count[left_char] -= 1
                
                if window_count[left_char] == 0:
                    del window_count[left_char]
                
                left += 1
            if window_count == s1_count:
                return True
        
        return False


# -------------------------------
# PARALLEL DRY RUN (IMPORTANT)
# -------------------------------
# s1 = "ab"
# s2 = "eidbaooo"
#
# s1_count = {a:1, b:1}
#
# right=0 → 'e'
# window={e:1}
#
# right=1 → 'i'
# window={e:1, i:1}
#
# right=2 → 'd'
# window={e:1, i:1, d:1}
# shrink → remove 'e'
# window={i:1, d:1}
#
# right=3 → 'b'
# window={i:1, d:1, b:1}
# shrink → remove 'i'
# window={d:1, b:1}
#
# right=4 → 'a'
# window={d:1, b:1, a:1}
# shrink → remove 'd'
# window={b:1, a:1}
#
# match found → return True
# -------------------------------