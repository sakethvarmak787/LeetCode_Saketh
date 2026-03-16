class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) 
        created_range = list(range(length+1))
        res = 0
        for i in created_range:
            if created_range[i] not in nums:
                res = created_range[i]

        return res
