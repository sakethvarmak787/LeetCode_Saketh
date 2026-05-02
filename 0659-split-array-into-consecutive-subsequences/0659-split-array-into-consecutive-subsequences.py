from collections import Counter

class Solution:
    def isPossible(self, nums):
        freq = Counter(nums)
        need = Counter()
        
        for num in nums:
            if freq[num] == 0:
                continue
            
            # Use this number
            freq[num] -= 1
            
            # Case 1: extend existing sequence
            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1
            
            # Case 2: create new sequence
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] += 1
            
            else:
                return False
        
        return True