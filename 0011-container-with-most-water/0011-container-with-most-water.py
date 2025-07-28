class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            ht = min(height[left], height[right])
            area = ht * width
            max_water = max(max_water, area)

            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
