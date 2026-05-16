from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        res = []

        left = 0

        window = SortedList()

        for right in range(len(nums)):

            # add current element
            window.add(nums[right])

            # valid window formed
            if right - left + 1 == k:

                # odd length
                if k % 2 == 1:

                    median = window[k // 2]

                # even length
                else:

                    median = (
                        window[k // 2] +
                        window[(k // 2) - 1]
                    ) / 2

                res.append(median)

                # remove left element
                window.remove(nums[left])

                left += 1

        return res