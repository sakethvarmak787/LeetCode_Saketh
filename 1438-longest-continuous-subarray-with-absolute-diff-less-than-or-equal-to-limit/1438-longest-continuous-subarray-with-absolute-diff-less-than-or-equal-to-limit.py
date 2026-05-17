from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        l = 0
        longest = 0
        maxdq = deque()
        mindq = deque()

        for r in range(len(nums)):
            while maxdq and nums[r] > maxdq[-1]:
                maxdq.pop()
            maxdq.append(nums[r])
            while mindq and nums[r] < mindq[-1]:
                mindq.pop()
            mindq.append(nums[r])
            while maxdq[0] - mindq[0] > limit:
                if nums[l] == maxdq[0]:
                    maxdq.popleft()
                if nums[l] == mindq[0]:
                    mindq.popleft()
                l += 1
            longest = max(longest, r - l + 1)
        return longest