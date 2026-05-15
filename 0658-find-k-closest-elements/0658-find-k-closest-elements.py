class Solution:
    def findClosestElements(self, arr, k, x):
        
        pairs = []
        for num in arr:
            distance = abs(num - x)
            pairs.append((distance, num))
        
        pairs.sort()
        closest = pairs[:k]
        
        result = []
        for dist, num in closest:
            result.append(num)
        
        result.sort()
    
        
        return result