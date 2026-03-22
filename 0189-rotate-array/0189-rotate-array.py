class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        nums1 = nums[n-k:]
        nums2 = nums[:n-k]

        nums[:] = nums1 + nums2  