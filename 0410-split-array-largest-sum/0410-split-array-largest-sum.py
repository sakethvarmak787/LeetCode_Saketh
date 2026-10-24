class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left+right) // 2 #(10+32) // 2 = 42 // 2  = 21
            subarrays = 1
            current_sum = 0 # tracks the current sum
            for num in nums: 
                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num

            if subarrays <= k:
                right = mid
            else:
                left = mid +1
        return left

            

