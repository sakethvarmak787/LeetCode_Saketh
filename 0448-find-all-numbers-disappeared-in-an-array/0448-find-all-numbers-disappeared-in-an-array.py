class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        nums_set = set(nums)

        missing = 1
        res = []

        while missing <= len(nums):

            if missing not in nums_set:
                res.append(missing)

            missing += 1

        return res