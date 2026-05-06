class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxprod = nums[0]
        currmax = nums[0]
        currmin = nums[0]

        for i in range(1, len(nums)):

            temp = currmax

            currmax = max(nums[i],
                          currmax * nums[i],
                          currmin * nums[i])

            currmin = min(nums[i],
                          temp * nums[i],
                          currmin * nums[i])

            maxprod = max(maxprod, currmax)

        return maxprod