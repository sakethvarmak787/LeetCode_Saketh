class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # if mid element is greater than right,
            # minimum is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # minimum is in left half (including mid)
                right = mid

        return nums[left]