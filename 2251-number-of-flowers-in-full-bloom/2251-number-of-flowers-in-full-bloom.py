from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        starts = sorted(start for start, end in flowers)
        ends = sorted(end for start, end in flowers)

        answer = []

        for t in people:

            started = bisect_right(starts, t)

            ended = bisect_left(ends, t)

            answer.append(started - ended)

        return answer