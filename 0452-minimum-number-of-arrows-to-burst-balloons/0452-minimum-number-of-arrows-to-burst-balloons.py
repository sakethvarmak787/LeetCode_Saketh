class Solution:
    def findMinArrowShots(self, points): 
        
        points.sort(key=lambda x: x[0])
        arrows = 1
        prev_start, prev_end = points[0]
        
        for curr_start, curr_end in points[1:]:
            
            # overlap
            if curr_start <= prev_end:
                prev_end = min(prev_end, curr_end)
            
            # no overlap → need new arrow
            else:
                arrows += 1
                prev_start, prev_end = curr_start, curr_end
        
        return arrows