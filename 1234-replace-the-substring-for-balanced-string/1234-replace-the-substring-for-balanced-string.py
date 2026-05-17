class Solution:
    def balancedString(self, s: str) -> int:

        ss = Counter(s)

        n = len(s)

        maxx = n // 4
        if (
            ss['Q'] == maxx and
            ss['W'] == maxx and
            ss['E'] == maxx and
            ss['R'] == maxx
        ):
            return 0

        left = 0

        ans = n

        for right in range(n):
            ss[s[right]] -= 1

            while (
                ss['Q'] <= maxx and
                ss['W'] <= maxx and
                ss['E'] <= maxx and
                ss['R'] <= maxx
            ):

                ans = min(ans, right - left + 1)

                ss[s[left]] += 1

                left += 1

        return ans