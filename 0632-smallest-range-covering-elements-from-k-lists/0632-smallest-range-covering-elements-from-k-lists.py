class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        min_heap = []
        current_max = float('-inf')
        for i in range(len(nums)):
            value = nums[i][0]
            heapq.heappush(min_heap,(value,i,0))
            current_max = max(current_max,value)
        best_start = min_heap[0][0]
        best_end = current_max
        while len(min_heap) == len(nums):
            current_min, list_idx, element_idx = heapq.heappop(min_heap)
            if (current_max - current_min < best_end - best_start or (current_max - current_min == best_end - best_start and current_min < best_start)):
                best_start = current_min
                best_end = current_max
            
            next_idx = element_idx + 1
            if next_idx == len(nums[list_idx]):
                break
            next_value = nums[list_idx][next_idx]
            heapq.heappush(min_heap,(next_value,list_idx, next_idx))
            current_max = max(current_max,next_value)
        return [best_start,best_end]



