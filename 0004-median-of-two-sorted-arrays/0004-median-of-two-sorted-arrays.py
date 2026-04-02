class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        res = sorted(nums1 + nums2)
        n = len(res)

        if n % 2 == 1:
            return float(res[n // 2])
        else:
            return (res[n // 2 - 1] + res[n // 2]) / 2