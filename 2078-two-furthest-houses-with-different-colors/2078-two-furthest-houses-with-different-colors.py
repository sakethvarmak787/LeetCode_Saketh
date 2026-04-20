class Solution:
    def maxDistance(self, colors):
        
        # Step 1: initialize the answer
        # This will store the maximum distance we find
        max_distance = 0
        
        # Step 2: loop over all possible first houses
        for i in range(len(colors)):
            
            # Step 3: for each i, try all possible second houses
            for j in range(len(colors)):
                
                # Step 4: check if the colors are different
                # We only care about pairs with different colors
                if colors[i] != colors[j]:
                    
                    # Step 5: compute the distance
                    distance = abs(i - j)
                    
                    # Step 6: update max_distance if this is larger
                    max_distance = max(max_distance, distance)
                    
                   
        
        # Step 7: return the final result
        return max_distance