import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)

        heap = []  
        sum1 = 0    
        res = 0   

        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            sum1 += n1
            if len(heap) > k:
                sum1 -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, sum1 * n2)

        return res