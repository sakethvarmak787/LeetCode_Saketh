import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        if not nums1 or not nums2:
            return []
        
        heap = []
        res = []
        
        # push first column (nums2[0]) with all nums1[i]
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        while heap and len(res) < k:
            total, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            
            # move to next element in nums2
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return res