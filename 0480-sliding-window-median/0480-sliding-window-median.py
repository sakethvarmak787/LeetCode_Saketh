from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        res = []

        left = 0

        window = SortedList()

        for right in range(len(nums)):
            window.add(nums[right])
            if right - left + 1 == k:
                if k % 2 == 1:

                    median = window[k // 2]
                else:

                    median = (
                        window[k // 2] +
                        window[(k // 2) - 1]
                    ) / 2

                res.append(median)

                window.remove(nums[left])

                left += 1

        return res