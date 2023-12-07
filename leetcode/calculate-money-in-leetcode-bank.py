class Solution:
    def totalMoney(self, n: int) -> int:
        mondays = n // 7
        left_days = n%7
        s = 1
        e = 8
        sums = 0
        if n <= 7:
            return sum(range(1,n+1))

        for _ in range(mondays):
            sums += sum(range(s,e))
            s += 1
            e += 1
        
        for _ in range(left_days):
            sums += s
            s += 1
        
        return sums

        
        