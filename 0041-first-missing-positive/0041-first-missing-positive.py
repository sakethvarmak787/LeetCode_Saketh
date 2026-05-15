class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = set(nums)
        missing = 1
        while missing in new:
            missing += 1
        return missing