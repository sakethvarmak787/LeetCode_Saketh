from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        # Step 1: Sort pairs based on their ending value
        # WHY: We want to always pick the pair that finishes earliest
        pairs.sort(key=lambda x: x[1])
        
        count = 0
        
        # This will track the end of the last chosen pair
        # Start with very small value so first pair always fits
        current_end = float('-inf')
        
        # Traverse all pairs
        for left, right in pairs:
            
            # Check if this pair can follow previous one
            # WHY: Only if it starts AFTER the last one ends
            if left > current_end:
                
                # Include this pair in chain
                count += 1
                
                # Update current_end to this pair's end
                current_end = right
                
                # ---- DRY RUN TRACE ----
                # Example: [[1,2],[2,3],[3,4]]
                #
                # Iteration 1: left=1, right=2
                # 1 > -inf → YES → pick
                # count = 1, current_end = 2
                #
                # Iteration 2: left=2, right=3
                # 2 > 2 → NO → skip
                #
                # Iteration 3: left=3, right=4
                # 3 > 2 → YES → pick
                # count = 2, current_end = 4
        
        return count