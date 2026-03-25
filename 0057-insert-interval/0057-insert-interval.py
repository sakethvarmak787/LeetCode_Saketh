class Solution:
    def insert(self, intervals, newInterval):
        res = []
        new_start, new_end = newInterval
        
        for start, end in intervals: 
           
            if end < new_start:
                res.append([start, end])
        
            elif start > new_end:
                res.append([new_start, new_end])
                new_start, new_end = start, end
            
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        
        res.append([new_start, new_end])
        
        return res