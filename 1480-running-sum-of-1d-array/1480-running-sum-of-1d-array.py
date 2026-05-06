class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        count = nums[0]
        res.append(count)
        for i in range(1,len(nums)):
            count = count + nums[i]
            res.append(count)

        return res
