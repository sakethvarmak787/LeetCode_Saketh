class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        numss = list(set(nums))   
        numss.sort(reverse=True)

        if len(numss) < 3:
            return numss[0]

        return numss[2]