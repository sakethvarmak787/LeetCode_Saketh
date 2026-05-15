class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        res = []
        for i in range(len(nums)):
            if hashmap[nums[i]] > 1 and nums[i] not in res:
                res.append(nums[i])

        return res

        


