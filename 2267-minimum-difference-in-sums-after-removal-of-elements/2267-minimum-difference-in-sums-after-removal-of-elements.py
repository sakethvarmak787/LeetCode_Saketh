from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        left = [0] * len(nums)
        right = [0] * len(nums)

        # Step 1: Track minimum sum of n elements from the left using max-heap
        max_heap = []
        left_sum = sum(nums[:n])
        for num in nums[:n]:
            heappush(max_heap, -num)
        left[n - 1] = left_sum

        for i in range(n, 2 * n):
            heappush(max_heap, -nums[i])
            left_sum += nums[i]
            removed = -heappop(max_heap)
            left_sum -= removed
            left[i] = left_sum

        # Step 2: Track maximum sum of n elements from the right using min-heap
        min_heap = []
        right_sum = sum(nums[-n:])
        for num in nums[-n:]:
            heappush(min_heap, num)
        right[2 * n] = right_sum

        for i in range(2 * n - 1, n - 1, -1):
            heappush(min_heap, nums[i])
            right_sum += nums[i]
            removed = heappop(min_heap)
            right_sum -= removed
            right[i] = right_sum

        # Step 3: Compute the minimum difference
        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            diff = left[i] - right[i + 1]
            min_diff = min(min_diff, diff)

        return min_diff
