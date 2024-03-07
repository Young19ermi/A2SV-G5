class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = close = 0

        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                open += 1
            elif s[i] == ')':
                if open != 0:
                    open -= 1
                else:
                    ans += 1
        return ans + open
        # stack = []
        # for n in s:
        #     if stack:
        #         if n == ")" and stack[-1] == "(":
        #             stack.pop()
        #             print(stack)
        #         elif stack[-1] == "(" and n == "(":
        #             stack.append(n)
        #         elif stack[-1] == ")" and n == ")":
        #             stack.append(n)
        #     else:
        #         stack.append(n)
        # return len(stack)
        