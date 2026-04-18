class Solution:
    def numFriendRequests(self, ages):
        # Step 1: Sort ages so that we can use ordering
        ages.sort()
        
        n = len(ages)
        left = 0   # left boundary of valid window
        right = 0  # right boundary of valid window
        total_requests = 0
        
        # Iterate each person as sender (x)
        for i in range(n):
            age_x = ages[i]
            
            # Ignore ages < 15 because they can never send requests
            # WHY: 0.5 * age + 7 will always block them
            if age_x < 15:
                continue
            
            # -------------------------------
            # Move LEFT pointer
            # -------------------------------
            # We move left until condition becomes valid
            # i.e., remove all people who are too young
            #
            # Example:
            # For age_x = 18:
            # 0.5 * 18 + 7 = 16
            # So we remove all ages <= 16
            while ages[left] <= 0.5 * age_x + 7:
                left += 1
            
            # -------------------------------
            # Move RIGHT pointer
            # -------------------------------
            # Expand right as long as people are <= age_x
            #
            # Example:
            # If age_x = 17:
            # We include all ages <= 17
            while right + 1 < n and ages[right + 1] <= age_x:
                right += 1
            
            # -------------------------------
            # Count valid people
            # -------------------------------
            # All valid y are in range [left, right]
            # We subtract 1 implicitly by doing (right - left)
            # because one of them is x itself
            #
            # Example:
            # ages = [16,17,18]
            #
            # i = 1 (age = 17)
            # left = 0, right = 1
            # valid = 1 (only 16)
            #
            total_requests += (right - left)
            
            # -------------------------------
            # Parallel dry run inside code:
            #
            # For ages = [16,17,18]:
            #
            # i = 0 → contributes 0
            # i = 1 → contributes 1
            # i = 2 → contributes 1
            #
            # total = 2
            # -------------------------------
        
        return total_requests