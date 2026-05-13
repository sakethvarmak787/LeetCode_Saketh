class Solution:
    def customSortString(self, order: str, s: str) -> str:

        ans = []
        for ch in order:

            for c in s:
                if c == ch:
                    ans.append(c)


        for c in s:

            if c not in order:
                ans.append(c)

        return ''.join(ans)