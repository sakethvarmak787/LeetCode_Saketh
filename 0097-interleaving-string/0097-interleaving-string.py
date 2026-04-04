class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # Step 1: Length check (very important)
        if len(s1) + len(s2) != len(s3):
            return False
        
        rows = len(s1) + 1
        cols = len(s2) + 1
        
        # Step 2: Create DP table
        dp = [[False] * cols for _ in range(rows)]
        
        # Step 3: Base case
        dp[0][0] = True
        
        # Step 4: Fill DP table
        for i in range(rows):
            for j in range(cols):
                
                # Case 1: Take character from s1
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                
                # Case 2: Take character from s2
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        
        # Step 5: Final answer
        return dp[len(s1)][len(s2)]