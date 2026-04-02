class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = []

        for i in range(len(nums)):
            if nums[i] not in res:
                res.append(nums[i])
            else:
                res.remove(nums[i])

        return res[0]