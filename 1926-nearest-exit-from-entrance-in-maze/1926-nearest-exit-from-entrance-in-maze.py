class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        rows = len(maze)
        cols = len(maze[0])

        r,c = entrance
        
        q = deque()
        q.append((r,c,0))

        visited = set()
        visited.add((r,c))

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            r,c,steps = q.popleft()

            if (r,c) != (entrance[0],entrance[1]) and (r==0 or c==0 or r==rows-1 or c==cols-1):
                return steps

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc

                if nr<0 or nc<0 or nr>=rows or nc>=cols:
                    continue
                if maze[nr][nc] == "." and (nr,nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, steps + 1))
        return -1

        
