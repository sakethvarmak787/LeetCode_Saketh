class Solution:
    def rotatedDigits(self, n: int) -> int:
        store = {0:0, 1:1, 8:8, 2:5, 5:2, 6:9, 9:6}
        count = 0

        for num in range(1, n + 1):
            digits = list(map(int, str(num)))
            new = []
            valid = True

            for d in digits:
                if d not in store:
                    valid = False
                    break
                new.append(store[d])

            if not valid:
                continue

            rotated = int("".join(map(str, new)))

            if rotated != num:
                count += 1

        return count