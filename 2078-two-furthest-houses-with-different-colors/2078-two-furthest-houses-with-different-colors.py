class Solution:
    def maxDistance(self, colors):
        
        n = len(colors)
        
        # Step 1: initialize answer
        max_distance = 0
        
        for i in range(n - 1, -1, -1):
            
            # Check if colors are different
            if colors[i] != colors[0]:
                
                max_distance = i
                break
        
        for i in range(n):
            
            if colors[i] != colors[n - 1]:
                
                # Distance = (n-1) - i
                max_distance = max(max_distance, (n - 1) - i)
                
                # Break because we found the farthest from this side
                break
            
          
        
        
        return max_distance