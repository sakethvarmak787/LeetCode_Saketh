class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        j = Counter(jewels)
        s = Counter(stones)

        for ch in jewels:
            if ch in stones:
                count += s[ch]

        return count
