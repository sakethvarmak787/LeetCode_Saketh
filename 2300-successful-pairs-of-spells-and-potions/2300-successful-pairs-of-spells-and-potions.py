import bisect

class Solution:
    def successfulPairs(self, spells, potions, success):        
        potions.sort()
        final = []
        n = len(potions)

        for i in spells:
            target = (success + i - 1) // i   
            idx = bisect.bisect_left(potions, target)
            
            count = n - idx
            final.append(count)

        return final