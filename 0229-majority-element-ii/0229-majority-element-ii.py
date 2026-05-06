class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

            if freq[num] > len(nums) // 3:
                res.append(num)

        final = list(set(res))
        return final
                