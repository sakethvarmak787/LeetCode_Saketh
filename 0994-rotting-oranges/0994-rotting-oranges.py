from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):

                
                if grid[r][c] == 2:
                    q.append((r,c))

                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0

        while q:

            size = len(q)

            for _ in range(size):

                r, c = q.popleft()

                
                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue

                    if grid[nr][nc] == 1:

                        grid[nr][nc] = 2
                        fresh -= 1

                        q.append((nr, nc))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes - 1
