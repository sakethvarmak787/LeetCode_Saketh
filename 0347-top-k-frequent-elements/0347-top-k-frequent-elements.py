from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        
        dictt = Counter(nums)

        arr = []
        
        for key in dictt:
            arr.append((dictt[key], key))
        
        arr.sort(reverse=True)
        
        res = []
        
        for i in range(k):
            res.append(arr[i][1])
        
        return res