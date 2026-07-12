class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new = sorted(arr)
        res = []
        n = 1
        d = {}

        for num in new:
            if num not in d:
                d[num] = n
                n += 1

        for num in arr:
            res.append(d[num])

        return res