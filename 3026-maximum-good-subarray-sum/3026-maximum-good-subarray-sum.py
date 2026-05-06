class Solution:
    def maximumSubarraySum(self, nums, k):

        mp = {}
        
        prefix = 0
        res = float('-inf')

        for num in nums:

            # case 1
            if num - k in mp:
                res = max(res, prefix + num - mp[num - k])

            # case 2
            if num + k in mp:
                res = max(res, prefix + num - mp[num + k])

            # store minimum prefix
            if num not in mp:
                mp[num] = prefix
            else:
                mp[num] = min(mp[num], prefix)

            prefix += num

        if res == float('-inf'):
            return 0

        return res