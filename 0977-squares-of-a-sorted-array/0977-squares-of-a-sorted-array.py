import heapq

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        heap = []
        for i in range(len(nums)):

            heapq.heappush(heap, nums[i] * nums[i])

        ans = []
        while heap:

            ans.append(heapq.heappop(heap))

        return ans