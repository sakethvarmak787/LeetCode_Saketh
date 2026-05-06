class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for ch in s:
            if ch == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(ch)

        ss = "".join(s_stack)

        for ch in t:
            if ch == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(ch)

        tt = "".join(t_stack)

        return ss == tt