class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        res1 = []
        res2 = []
        final = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for i in range(len(nums1)):
            if nums1[i]not in nums2:
                
                res1.append(nums1[i])
            
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                res2.append(nums2[i])
            
        final.append(res1)
        final.append(res2)

        return final
        