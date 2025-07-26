class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        t = True
        f = False

        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxx:
                res.append(t)
            else:
                res.append(f)
        return res
