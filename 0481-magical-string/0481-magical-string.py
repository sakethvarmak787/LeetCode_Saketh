class Solution:
    def magicalString(self, n: int) -> int:
        
        # Edge case:
        # If n is 0, there are no elements, so no '1's
        if n == 0:
            return 0
        
        # Start with the base magical string
        # This is given and always correct starting point
        s = [1, 2, 2]
        
        # Pointer i:
        # This tells us how many times we need to repeat the next number
        # Initially pointing to index 2
        i = 2
        
        # This is the next number we will append
        # Since last number in s is 2, next should be 1
        next_num = 1
        
        # -------------------------
        # BUILD THE STRING
        # -------------------------
        # Keep building until we have at least n elements
        while len(s) < n:
            
            # How many times to append?
            # Look at current pointer i
            count = s[i]
            
            # Append next_num 'count' times
            for _ in range(count):
                s.append(next_num)
                
                # ---- Parallel Dry Run (n = 6) ----
                # Initially:
                # s = [1, 2, 2]
                # i = 2 → s[i] = 2 → append '1' twice
                
                # After 1st append:
                # s = [1, 2, 2, 1]
                
                # After 2nd append:
                # s = [1, 2, 2, 1, 1]
                
                # Next iteration:
                # i = 3 → s[i] = 1 → append '2' once
                
                # s = [1, 2, 2, 1, 1, 2]
            
            # After appending, flip the number
            # If it was 1 → make it 2
            # If it was 2 → make it 1
            next_num = 2 if next_num == 1 else 1
            
            # Move pointer forward
            i += 1
        
        # -------------------------
        # COUNT NUMBER OF 1's
        # -------------------------
        count_ones = 0
        
        # Only consider first n elements
        for j in range(n):
            if s[j] == 1:
                count_ones += 1
        
        return count_ones