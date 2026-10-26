class Solution:
    def canCross(self, stones: list[int]) -> bool:
        dp = {stone:set() for stone in stones}
        #0:set(),1:set(),3:set()
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                for jump in (k-1,k,k+1):
                    if jump > 0:
                        next_stone = stone + jump
                        if next_stone in dp:
                            dp[next_stone].add(jump)

        return len(dp[stones[-1]]) > 0