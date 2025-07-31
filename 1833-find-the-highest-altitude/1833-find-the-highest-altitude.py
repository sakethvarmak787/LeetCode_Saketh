class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        add_val = 0
        for i in range(len(gain)):
            add_val = add_val + gain[i]
            res.append(add_val)

        return max(res)