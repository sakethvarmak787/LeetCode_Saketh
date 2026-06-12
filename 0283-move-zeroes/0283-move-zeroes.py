class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        res = [0] *len(nums)
        l = 0
        r = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                r-=1
            else:
                res[l] = nums[i]
                l+=1
        for i in range(len(nums)):
            nums[i] = res[i]
                
                
       