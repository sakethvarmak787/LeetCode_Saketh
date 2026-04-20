class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        
        # Step 1: Build a decreasing stack of indices
        stack = []
        
        # We want indices where values are strictly decreasing
        # Why? Because these are the best candidates for 'i'
        for i in range(n):
            # If stack is empty OR current value is smaller than last stacked value
            # then this index is useful
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # At this point, stack contains indices like:
        # [0, 1] for example → values [6, 0]
        # These are best starting points
        
        max_width = 0
        
        # Step 2: Traverse from right to left
        for j in range(n - 1, -1, -1):
            
            # Try to match current j with best i from stack
            while stack and nums[stack[-1]] <= nums[j]:
                
                i = stack.pop()  # candidate start
                
                # Calculate width
                width = j - i
                
                # Update maximum width
                if width > max_width:
                    max_width = width
        
        return max_width