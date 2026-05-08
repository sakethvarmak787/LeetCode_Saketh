import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        # Count frequencies and push into a Max-Heap
        # Python's heapq is a min-heap, so use negative counts
        max_heap = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(max_heap)
        
        prev_count, prev_char = 0, ""
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)
            
            # If there was a character waiting to be put back, push it now
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            # Decrement current count and set as "waiting"
            count += 1 
            prev_count, prev_char = count, char
            
        result_str = "".join(res)
        return result_str if len(result_str) == len(s) else ""