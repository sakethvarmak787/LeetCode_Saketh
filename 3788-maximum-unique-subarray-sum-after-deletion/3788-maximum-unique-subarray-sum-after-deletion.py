class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = []
        
        if all(num < 0 for num in nums):
            return max(nums)

        
        for i in range(len(nums)):
            if len(nums) == 1:
                return nums[i]
    
            if nums[i] not in res and nums[i]>0:
                res.append(nums[i])
        
    
        return sum(res)