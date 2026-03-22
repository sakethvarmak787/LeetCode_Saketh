class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # edge case
        if numRows == 1:
            return s

        rows = [""] * numRows   # store each row
        curr_row = 0            # current row
        direction = 1           # 1 = down, -1 = up

        for char in s:
            rows[curr_row] += char   # put char in current row

            # change direction at boundaries
            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction   # move to next row

        return "".join(rows)