class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # If s1 is longer, impossible case
        if len(s1) > len(s2):
            return False
        
        # Step 1: Build frequency map of s1
        s1_count = {}
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1
        
        # Window frequency map
        window_count = {}
        
        left = 0
        
        # Traverse s2 using right pointer
        for right in range(len(s2)):
            
            # Add current character to window
            ch = s2[right]
            window_count[ch] = window_count.get(ch, 0) + 1
            
            # -------------------------------
            # WHY we shrink:
            # Because window must be same size as s1
            # -------------------------------
            if right - left + 1 > len(s1):
                
                # Remove left character
                left_char = s2[left]
                window_count[left_char] -= 1
                
                # Clean up zero count to keep map small
                if window_count[left_char] == 0:
                    del window_count[left_char]
                
                left += 1
            
            # -------------------------------
            # Check if window matches s1
            # -------------------------------
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