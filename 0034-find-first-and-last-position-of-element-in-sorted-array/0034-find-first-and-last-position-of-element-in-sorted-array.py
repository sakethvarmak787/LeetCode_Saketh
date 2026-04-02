class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst(nums, target):
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1   # we might find earlier mid, so dont stop
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def findLast(nums, target):
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1   
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first, last]
