from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        
        # 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses
        
        def dfs(course):
            
            # cycle detected
            if visit[course] == 1:
                return False
            
            # already checked
            if visit[course] == 2:
                return True
            
            # mark as visiting
            visit[course] = 1
            
            # check all prerequisites
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            
            # mark as done
            visit[course] = 2
            return True
        
        # check all courses
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True