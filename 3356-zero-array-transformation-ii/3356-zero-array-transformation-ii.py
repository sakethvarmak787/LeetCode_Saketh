class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        n = len(nums)

        def canMake(k):

            diff = [0] * (n + 1)

            for i in range(k):
                l, r, val = queries[i]

                diff[l] += val

                if r + 1 < n:
                    diff[r + 1] -= val

            coverage = 0

            for i in range(n):
                coverage += diff[i]

                if nums[i] > coverage:
                    return False

            return True

        if not canMake(len(queries)):
            return -1

        left = 0
        right = len(queries)

        ans = len(queries)

        while left <= right:

            mid = (left + right) // 2

            if canMake(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans