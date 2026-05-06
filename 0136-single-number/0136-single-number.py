class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        new = Counter(nums) #{1:1}
        for i in range(len(nums)):
            if new[nums[i]] ==1:
                return nums[i]