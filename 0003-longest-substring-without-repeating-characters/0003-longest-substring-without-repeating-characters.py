class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()   # store current window characters
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            
            # if duplicate ---> shrink window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # add current character
            char_set.add(s[right])
            
            # update max length
            max_len = max(max_len, right - left + 1)
        
        return max_len