class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        one = [0] * n
        zero = [0] * n

        for i in range(n):
            if s[i] == '1':
                one[i] += 1
            else:
                zero[i] += 1
            if i:
                one[i] += one[i - 1] 
            else:
                0
            if i:
                zero[i] += zero[i - 1] 
            else:
                0

        res = 0

        for i in range(1, n - 1):
            if s[i] == '1':
                res += zero[i - 1] * (zero[-1] - zero[i])
            else:
                res += one[i - 1] * (one[-1] - one[i])

        return res