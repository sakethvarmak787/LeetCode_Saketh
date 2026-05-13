class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        A,B,C,D = nums1,nums2,nums3,nums4
        res, complement = 0, collections.defaultdict(int)
        for a in A:
            for b in B:
                complement[a+b] += 1
        for c in C:
            for d in D:
                res += complement[-(c+d)]
        return res
        