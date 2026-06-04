class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)

        diff = [0] * (n + 1)

        for start, end, direction in shifts:

            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1

            else:
                diff[start] -= 1
                diff[end + 1] += 1

        shift = 0
        ans = []

        for i in range(n):

            shift += diff[i]

            pos = ord(s[i]) - ord('a')

            pos = (pos + shift) % 26

            ans.append(chr(pos + ord('a')))

        return "".join(ans)