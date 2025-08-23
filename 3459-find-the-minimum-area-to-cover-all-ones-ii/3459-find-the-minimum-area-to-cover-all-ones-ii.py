class Solution:
    def minimumSum(self, grid: list[list[int]]) -> int:
        """
        Finds the minimum possible sum of the area of three non-overlapping rectangles
        that cover all the 1s in a 2D binary array.

        Args:
            grid: A 2D binary array.

        Returns:
            The minimum possible sum of the area of three rectangles.
        """
        rows, cols = len(grid), len(grid[0])
        ones = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ones.append((r, c))

        if len(ones) < 3:
            
            return 0

        min_r, max_r = float('inf'), float('-inf')
        min_c, max_c = float('inf'), float('-inf')
        for r, c in ones:
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)

        def calculate_area(sub_grid, r1, r2, c1, c2):
            """Calculates the area of the bounding box of 1s in a sub-grid."""
            sub_ones_min_r, sub_ones_max_r = float('inf'), float('-inf')
            sub_ones_min_c, sub_ones_max_c = float('inf'), float('-inf')
            
            found_one = False
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if sub_grid[r][c] == 1:
                        sub_ones_min_r = min(sub_ones_min_r, r)
                        sub_ones_max_r = max(sub_ones_max_r, r)
                        sub_ones_min_c = min(sub_ones_min_c, c)
                        sub_ones_max_c = max(sub_ones_max_c, c)
                        found_one = True

            if not found_one:
                return 0
            
            return (sub_ones_max_r - sub_ones_min_r + 1) * (sub_ones_max_c - sub_ones_min_c + 1)

        min_total_area = float('inf')

        
        for r1 in range(min_r, max_r):
            for r2 in range(r1 + 1, max_r):
                area1 = calculate_area(grid, min_r, r1, min_c, max_c)
                area2 = calculate_area(grid, r1 + 1, r2, min_c, max_c)
                area3 = calculate_area(grid, r2 + 1, max_r, min_c, max_c)
                if area1 > 0 and area2 > 0 and area3 > 0:
                    min_total_area = min(min_total_area, area1 + area2 + area3)

        
        for c1 in range(min_c, max_c):
            for c2 in range(c1 + 1, max_c):
                area1 = calculate_area(grid, min_r, max_r, min_c, c1)
                area2 = calculate_area(grid, min_r, max_r, c1 + 1, c2)
                area3 = calculate_area(grid, min_r, max_r, c2 + 1, max_c)
                if area1 > 0 and area2 > 0 and area3 > 0:
                    min_total_area = min(min_total_area, area1 + area2 + area3)

        
        for r in range(min_r, max_r):
            
            for c in range(min_c, max_c):
                area1 = calculate_area(grid, min_r, r, min_c, c)
                area2 = calculate_area(grid, min_r, r, c + 1, max_c)
                area3 = calculate_area(grid, r + 1, max_r, min_c, max_c)
                if area1 > 0 and area2 > 0 and area3 > 0:
                    min_total_area = min(min_total_area, area1 + area2 + area3)

            for c in range(min_c, max_c):
                area1 = calculate_area(grid, min_r, r, min_c, max_c)
                area2 = calculate_area(grid, r + 1, max_r, min_c, c)
                area3 = calculate_area(grid, r + 1, max_r, c + 1, max_c)
                if area1 > 0 and area2 > 0 and area3 > 0:
                    min_total_area = min(min_total_area, area1 + area2 + area3)

       
        for c in range(min_c, max_c):
           
            for r in range(min_r, max_r):
                area1 = calculate_area(grid, min_r, r, min_c, c)
                area2 = calculate_area(grid, r + 1, max_r, min_c, c)
                area3 = calculate_area(grid, min_r, max_r, c + 1, max_c)
                if area1 > 0 and area2 > 0 and area3 > 0:
                    min_total_area = min(min_total_area, area1 + area2 + area3)

           
            for r in range(min_r, max_r):
                area1 = calculate_area(grid, min_r, max_r, min_c, c)
                area2 = calculate_area(grid, min_r, r, c + 1, max_c)
                area3 = calculate_area(grid, r + 1, max_r, c + 1, max_c)
                if area1 > 0 and area2 > 0 and area3 > 0:
                    min_total_area = min(min_total_area, area1 + area2 + area3)

        return min_total_area