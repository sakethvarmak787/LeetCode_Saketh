class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a=set(nums1)
        b=set(nums2)
        c=sorted(list(a.intersection(b)))
      
        if c:
            return c[0]
        return -1