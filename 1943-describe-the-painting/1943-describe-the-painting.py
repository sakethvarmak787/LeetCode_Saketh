from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:

        diff = defaultdict(int)

        for start, end, color in segments:
            diff[start] += color
            diff[end] -= color

        points = sorted(diff.keys())

        answer = []

        curr = 0

        for i in range(len(points) - 1):

            curr += diff[points[i]]

            left = points[i]
            right = points[i + 1]

            if curr > 0:
                answer.append([left, right, curr])

        return answer