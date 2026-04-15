class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        n = len(num)
        
        # We only try all possible first and second numbers
        # But after that, we DO NOT restart scanning → we move forward once
        
        for i in range(1, n):
            for j in range(i + 1, n):
                
                first_str = num[:i]
                second_str = num[i:j]
                
                # ------------------------------
                # Reject leading zero cases
                # ------------------------------
                # If number starts with '0' but length > 1 → invalid
                if (first_str.startswith('0') and len(first_str) > 1) or \
                   (second_str.startswith('0') and len(second_str) > 1):
                    continue
                
                # convert to integers
                first = int(first_str)
                second = int(second_str)
                
                # pointer where we start matching
                k = j
                
                # Example dry run:
                # num = "199100199"
                # i=1 → first="1"
                # j=3 → second="99"
                # k=3
                
                while k < n:
                    
                    # expected next number
                    next_num = first + second
                    next_str = str(next_num)
                    
                    length = len(next_str)
                    
                    # Example:
                    # first=1, second=99 → next=100
                    # check num[3:6] == "100"
                    
                    # ------------------------------
                    # If mismatch → stop early
                    # ------------------------------
                    if num[k:k + length] != next_str:
                        break
                    
                    # ------------------------------
                    # Move forward in sequence
                    # ------------------------------
                    # shift window:
                    # first ← second
                    # second ← next
                    
                    first = second
                    second = next_num
                    
                    # move pointer
                    k += length
                    
                    # Example progression:
                    # k=3 → match "100" → k=6
                    # k=6 → match "199" → k=9
                    
                # If we used entire string → success
                if k == n:
                    return True
        
        return False