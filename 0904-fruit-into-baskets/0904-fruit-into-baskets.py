class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        seen = {}

        l = 0
        maxx = 0

        for r in range(len(fruits)):
            seen[fruits[r]] = seen.get(fruits[r], 0) + 1
            while len(seen) > 2:
                seen[fruits[l]] -= 1

                if seen[fruits[l]] == 0:
                    del seen[fruits[l]]

                l += 1
            maxx = max(maxx, r - l + 1)

        return maxx