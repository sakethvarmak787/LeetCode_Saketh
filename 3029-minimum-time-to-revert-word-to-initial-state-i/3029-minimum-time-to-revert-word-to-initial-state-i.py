class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        
        n = len(word)
        
        # we simulate time step by step
        # but instead of brute force, we only check prefix match
        
        time = 1
        
        while True:
            
            # calculate how many characters we have removed so far
            start = time * k
            
            # if we removed entire string
            # remaining becomes empty → always matches
            if start >= n:
                return time
            
            # remaining part after removal
            remaining = word[start:]
            
            # prefix of same length
            prefix = word[:n - start]
            
            # check if remaining matches prefix
            # this ensures we can rebuild original string
            if remaining == prefix:
                return time
            
            # move to next second
            time += 1