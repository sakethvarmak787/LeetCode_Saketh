from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        res = []

        left = 0

        dq = deque()

        for right in range(n):

            # remove smaller elements
            while dq and nums[dq[-1]] < nums[right]:

                dq.pop()

            # add current index
            dq.append(right)

            # remove outside window indexes
            if dq[0] < left:

                dq.popleft()

            # valid window formed
            if right - left + 1 == k:

                maxx = nums[dq[0]]

                res.append(maxx)

                left += 1

        return res