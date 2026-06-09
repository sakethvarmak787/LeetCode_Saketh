class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        remove = 0

        for start, finish in intervals[1:]:

            if start < end:
                remove += 1
            else:
                end = finish

        return remove