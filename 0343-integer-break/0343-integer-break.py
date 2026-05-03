class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}

        def dfs(num):
            if num in memo:
                return memo[num]

            # base case
            if num == 1:
                return 1

            max_prod = 0

            for i in range(1, num):
                # either break further OR stop here
                max_prod = max(
                    max_prod,
                    i * (num - i),        # no further split
                    i * dfs(num - i)      # further split
                )

            memo[num] = max_prod
            return max_prod

        return dfs(n)