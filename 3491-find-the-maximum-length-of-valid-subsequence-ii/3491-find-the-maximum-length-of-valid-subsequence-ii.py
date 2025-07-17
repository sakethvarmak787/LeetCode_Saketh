

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        data = [ [0]*k for i in range(k) ]
        res = 0
        for n in nums:
            curr = n % k
            for rem in range(k):
                data[rem][curr] = data[curr][rem] + 1
                res = max(res, data[rem][curr])
        return res
