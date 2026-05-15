class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        n = len(blocks)

        mincount = float('inf')

        count = 0

        # first window
        for i in range(k):

            if blocks[i] == "W":
                count += 1

        mincount = count

        left = 0

        # slide window
        for right in range(k, n):

            # remove left element
            if blocks[left] == "W":
                count -= 1

            left += 1

            # add right element
            if blocks[right] == "W":
                count += 1

            mincount = min(mincount, count)

        return mincount