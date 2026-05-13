class Solution:
    def customSortString(self, order: str, s: str) -> str:

        ans = []

        # First put chars according to order
        for ch in order:

            for c in s:

                if c == ch:
                    ans.append(c)

        # Then put remaining chars
        for c in s:

            if c not in order:
                ans.append(c)

        return ''.join(ans)