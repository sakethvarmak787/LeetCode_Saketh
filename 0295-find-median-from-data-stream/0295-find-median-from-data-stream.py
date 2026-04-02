import heapq

class MedianFinder:

    def __init__(self):
        # max heap (store negatives)
        self.small = []
        # min heap
        self.large = []

    def addNum(self, num: int) -> None:
        # step 1: push into max heap
        heapq.heappush(self.small, -num)

        # step 2: ensure ordering property
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # step 3: balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # odd length
        if len(self.small) > len(self.large):
            return -self.small[0]

        # even length
        return (-self.small[0] + self.large[0]) / 2