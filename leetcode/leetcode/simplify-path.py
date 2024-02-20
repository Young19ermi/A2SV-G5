class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dir = path.split("/")
        for d in dir:
            if not d or d == ".":
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return "/" + "/".join(stack)                  