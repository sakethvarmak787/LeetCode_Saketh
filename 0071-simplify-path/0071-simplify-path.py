class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split('/') #this looks liks: 
        #lst = ["", "...", "", "a", "..", "b", "c", "..", "d", ".", ""]
        stack = []

        for d in lst:
            if d == "..":
                if stack:         #if stack is not empty then only append
                    stack.pop()
            elif d != "" and d != ".":
                stack.append(d)

        return "/" + "/".join(stack)