class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []

        for ch in s:

            # if top of stack and current char same
            if stack and stack[-1] == ch:
                stack.pop()

            else:
                stack.append(ch)

        return "".join(stack)