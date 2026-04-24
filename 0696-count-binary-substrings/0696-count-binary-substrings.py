class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        # This will store the length of the previous group
        prev_group = 0
        
        # This will store the length of the current group
        curr_group = 1  # start with first character
        
        result = 0
        
        # Start from second character
        for i in range(1, len(s)):
            
            # If same as previous character → still in same group
            if s[i] == s[i - 1]:
                curr_group += 1
            else:
                # Group changed (0 → 1 or 1 → 0)
                
                # Now we have two groups:
                # prev_group and curr_group
                # valid substrings = min(prev_group, curr_group)
                result += min(prev_group, curr_group)
                
                # Move current group to previous
                prev_group = curr_group
                
                # Reset current group
                curr_group = 1
        
        # After loop ends, we still have one last pair to consider
        result += min(prev_group, curr_group)
        
        return result