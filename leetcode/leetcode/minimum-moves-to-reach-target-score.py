class Solution:
    def minMoves(self, target: int, maxdoubles: int) -> int:
        oper = 0
        mul = 0
        res = 0
        if maxdoubles == 0:
            return target - 1
        if target == 1:
            return 0
        odd = True
        even = True
        res = 0
        while mul < maxdoubles and target != 1:
            if target % 2 != 0:
                target -= 1
                oper += 1
            else:
                target  = target // 2
                mul += 1
        res += mul + oper + target - 1
        return res

