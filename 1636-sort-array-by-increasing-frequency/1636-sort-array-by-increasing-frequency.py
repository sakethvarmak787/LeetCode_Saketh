class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        count = Counter(nums)

        ans = []

        for num, freq in sorted(count.items(), key=lambda x: (x[1], -x[0])):

            ans.extend([num] * freq)

        return ans