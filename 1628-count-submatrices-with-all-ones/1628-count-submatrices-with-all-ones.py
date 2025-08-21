from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        height = [0] * n
        total_submatrices = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

            
            for j in range(n):
                min_height = height[j]
                for k in range(j, -1, -1):
                    min_height = min(min_height, height[k])
                    total_submatrices += min_height

        return total_submatrices