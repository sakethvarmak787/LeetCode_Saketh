class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        a =sorted(nums)
        b = sorted(nums,reverse = True)

        if a==nums or b==nums:
            return True
        else:
            return False

