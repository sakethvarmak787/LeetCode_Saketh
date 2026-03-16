class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        target = len(nums) - k
        return nums[target]