class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        if n == 2:
            return 20
        even = n//2
        odd = n//2 + n%2
        result = (pow(5, odd, 10**9+7) * pow(4, even, 10**9+7)) % (10**9+7)
        return result
        # if n % 2 != 0:
        #     return (pow(pow(5,n//4, 10**),2)%(pow(10,9) + 7) * pow(pow(4, n//4),2) % (pow(10,9) + 7)#(x * pow(x, n-1)) % (pow(10,9) + 7)
        # if n % 2 == 0:
        #     return pow((pow(5,n//4),2)%(pow(10,9) + 7) * pow(pow(4, n//4),2) % (pow(10,9) + 7)
        # return pow(x,n/2) ** 2
        # def solution(n):
        #     if n % 2 == 0:
        #         return (pow(5,n//2)%(pow(10,9) + 7) * self.powr(4, n//2)) % (pow(10,9) + 7)
        #     else:
        #         return (pow(5, (n+1)//2)%(pow(10,9) + 7) * self.power(4, n//2)) % (pow(10,9) + 7)
        # return solution(n % (pow(10,9) + 7))