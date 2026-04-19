class Solution:
    def findNthDigit(self, n: int) -> int:
        
        # Step 1: Identify which group (1-digit, 2-digit, 3-digit...)
        digit_length = 1   # numbers with 1 digit initially
        count = 9          # 9 numbers: 1 to 9
        start = 1          # first number in this group
        
        # We keep reducing n until we find the correct group
        while n > digit_length * count:
            
            # ---- THINKING ----
            # We are skipping an entire group of numbers
            # because the n-th digit is not in this group
            # ------------------
            
            n -= digit_length * count   # remove all digits in this group
            
            digit_length += 1           # move to next group (2-digit, 3-digit...)
            count *= 10                # 9 → 90 → 900 → ...
            start *= 10                # 1 → 10 → 100 → ...
        
        # ---- PARALLEL DRY RUN (n = 11) ----
        # Initially: n = 11
        # Skip 1-digit group → n = 2
        # Now in 2-digit group (start = 10)
        # -----------------------------------
        
        
        # Step 2: Find the exact number in this group
        
        # (n - 1) because indexing is 0-based
        index = (n - 1) // digit_length
        
        number = start + index
        
        # ---- DRY RUN ----
        # index = (2-1)//2 = 0
        # number = 10
        # ------------------
        
        
        # Step 3: Find the exact digit inside that number
        
        digit_index = (n - 1) % digit_length
        
        # Convert number to string to access digit
        result_digit = str(number)[digit_index]
        
        # ---- DRY RUN ----
        # digit_index = (2-1)%2 = 1
        # number = "10"
        # result = "0"
        # ------------------
        
        return int(result_digit)