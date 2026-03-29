from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build graph
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        visit = [0] * numCourses
        res = []

        def dfs(course):

            # cycle
            if visit[course] == 1:
                return False

            # already done
            if visit[course] == 2:
                return True

            visit[course] = 1

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            visit[course] = 2

            res.append(course)  

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res