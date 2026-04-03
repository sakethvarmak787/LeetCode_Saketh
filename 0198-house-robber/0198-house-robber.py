class Solution:
    def rob(self, nums):
        
        if len(nums) == 1:
            return nums[0]
        
        two_houses_before = 0   # dp[i-2]
        one_house_before = 0    # dp[i-1]
        # if we rob curr house, then we cant ronb previous , we must tak i-2 house to rob
        for money in nums:
            current = max(
                money + two_houses_before,  # rob current
                one_house_before            # skip current
            )
            
            # shift forward
            two_houses_before = one_house_before
            one_house_before = current
        
        return one_house_before