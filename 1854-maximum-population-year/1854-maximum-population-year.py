from collections import defaultdict

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        diff = defaultdict(int)

        for birth, death in logs:
            diff[birth] += 1
            diff[death] -= 1

        curr = 0
        max_pop = 0
        answer = 0

        for year in sorted(diff):

            curr += diff[year]

            if curr > max_pop:
                max_pop = curr
                answer = year

        return answer