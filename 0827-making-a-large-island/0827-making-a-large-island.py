class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n= len(grid)
        island_size = {}
        island_id = 2
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(row,col,island_id):
            stack = [(row,col)]
            grid[row][col] = island_id
            area = 1
            while stack:
                r,c = stack.pop()
                for dr,dc in directions:
                    nr = r +dr
                    nc = c+dc
                    if (0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1):
                        grid[nr][nc] = island_id
                        stack.append((nr,nc))
                        area += 1
            return area
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    island_size[island_id] = dfs(row,col,island_id)
                    island_id += 1

        max_area = max(island_size.values(),default = 0)
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    neighbours =set()
                    for dr,dc in directions:
                        nr = row + dr
                        nc = col + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            neighbour_id = grid[nr][nc]
                            if neighbour_id > 1:
                                neighbours.add(neighbour_id)
                    area = 1
                    max_area = max(max_area,area) #start with 1 for water cell, that wewee are thinking to flip
                    for id in neighbours:
                        area += island_size[id]
                        max_area = max(max_area,area)
        return max_area



        