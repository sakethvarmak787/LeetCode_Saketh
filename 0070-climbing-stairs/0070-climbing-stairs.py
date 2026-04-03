class Solution:
    def climbStairs(self, n: int) -> int:
        
        # base cases
        if n <= 2:
            return n
        #ways(n-1) + ways(n-2)
        one_step_before = 2   # ways to reach (n-1)
        two_steps_before = 1  # ways to reach (n-2)
        
        for i in range(3, n + 1):
            current = one_step_before + two_steps_before
            
            # shift forward
            two_steps_before = one_step_before
            one_step_before = current
        
        return one_step_before