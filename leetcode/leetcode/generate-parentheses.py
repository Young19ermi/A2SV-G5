class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def solve(s,l,r):
            if 2 * n == len(s):
                res.append(s )
                return 
            if l < n:
                solve(s+'(', l+1, r)
            if r < l:
                solve(s + ')', l ,r+1)

        solve('',0,0) 
        return res