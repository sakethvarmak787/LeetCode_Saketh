class Solution:
    def findClosestElements(self, arr, k, x):
        
        # Step 1: Create a list to store (distance, value)
        pairs = []
        
        # We go through each element and compute how far it is from x
        for num in arr:
            # distance tells how "close" this number is to x
            distance = abs(num - x)
            
            # store both distance and value so we can sort later
            pairs.append((distance, num))
        
        # Example dry run:
        # arr = [1,2,3,4,5], x = 3
        # pairs becomes:
        # [(2,1), (1,2), (0,3), (1,4), (2,5)]
        
        
        # Step 2: Sort pairs
        # Python will sort tuples like:
        # first by distance, then by value automatically
        pairs.sort()
        
        # After sorting:
        # [(0,3), (1,2), (1,4), (2,1), (2,5)]
        
        
        # Step 3: Take first k elements (closest ones)
        closest = pairs[:k]
        
        # If k = 4:
        # closest = [(0,3), (1,2), (1,4), (2,1)]
        
        
        # Step 4: Extract only the values (ignore distance)
        result = []
        for dist, num in closest:
            result.append(num)
        
        # result becomes:
        # [3,2,4,1]
        
        
        # Step 5: Sort final result (because output must be ascending)
        result.sort()
        
        # result becomes:
        # [1,2,3,4]
        
        
        return result