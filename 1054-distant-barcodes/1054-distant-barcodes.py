from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes):
        # -----------------------------------------------------------
        # Step 1: Count frequency of each number
        # WHY:
        # The whole problem depends on how many times a number appears.
        # The most frequent number is the most dangerous one.
        # -----------------------------------------------------------
        freq = Counter(barcodes)

        # -----------------------------------------------------------
        # Step 2: Sort numbers based on frequency (highest first)
        # WHY:
        # We want to place the most frequent numbers first,
        # so we can spread them out as much as possible.
        # -----------------------------------------------------------
        sorted_items = sorted(freq.items(), key=lambda x: -x[1])

        # Example:
        # barcodes = [1,1,1,2,2,2]
        # freq = {1:3, 2:3}
        # sorted_items = [(1,3), (2,3)]

        # -----------------------------------------------------------
        # Step 3: Create result array
        # -----------------------------------------------------------
        n = len(barcodes)
        res = [0] * n

        # Pointer to fill positions
        index = 0

        # -----------------------------------------------------------
        # Step 4: Fill numbers one by one
        # -----------------------------------------------------------
        for num, count in sorted_items:

            # Place 'num' exactly 'count' times
            while count > 0:

                # ---------------------------------------------------
                # Place number at current index
                # WHY:
                # We are filling even positions first (0,2,4...)
                # This ensures maximum spacing between same numbers
                # ---------------------------------------------------
                res[index] = num

                # Move index by 2 (skip one position)
                index += 2

                # If we go out of bounds, switch to odd indices
                if index >= n:
                    index = 1  # start filling gaps

                # Decrease count
                count -= 1

        return res


# -----------------------------------------------------------
# PARALLEL DRY RUN (example: [1,1,1,2,2,2])
# -----------------------------------------------------------

# freq = {1:3, 2:3}
# sorted_items = [(1,3), (2,3)]

# res = [_, _, _, _, _, _]
# index = 0

# Place 1:
# res[0] = 1 → index=2
# res[2] = 1 → index=4
# res[4] = 1 → index=6 → reset to 1

# res = [1, _, 1, _, 1, _]

# Place 2:
# res[1] = 2 → index=3
# res[3] = 2 → index=5
# res[5] = 2 → index=7 → reset

# res = [1,2,1,2,1,2]