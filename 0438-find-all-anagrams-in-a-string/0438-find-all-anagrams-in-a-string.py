class Solution:
    def findAnagrams(self, s: str, p: str):
        
        # This will store all valid starting indices
        result = []
        
        # Length of p (fixed window size)
        k = len(p)
        
        # Sort p once (this is our reference pattern)
        sorted_p = sorted(p)
        # Example:
        # p = "abc" → sorted_p = ['a','b','c']
        
        # Loop through s
        # We stop at len(s) - k because beyond that we cannot form a full window
        for i in range(len(s) - k + 1):
            
            # Step 1: Take substring of length k
            substring = s[i:i + k]
            
            # Example Dry Run:
            # s = "cbaebabacd", k = 3
            # i = 0 → substring = "cba"
            # i = 1 → substring = "bae"
            # i = 2 → substring = "aeb"
            
            # Step 2: Sort this substring
            sorted_sub = sorted(substring)
            
            # Example:
            # "cba" → ['a','b','c']
            # "bae" → ['a','b','e']
            
            # Step 3: Compare with sorted_p
            if sorted_sub == sorted_p:
                # If equal → this substring is an anagram
                
                # Store the starting index
                result.append(i)
                
                # Dry run:
                # i = 0 → match → result = [0]
                # i = 6 → match → result = [0,6]
        
        # Return final result
        return result