class Solution:
    # def fast(self, base, exponent):
    #         result = 1  
    #         while exponent > 0:
    #             if exponent & 1:
    #                 result = (result * base)
    #             base = (base * base) 
    #             exponent >>= 1
    #         return result

    # def myPow(self, x: float, n: int) -> float:
    #     if n < 0:
    #         return (1 / self.fast(x,n))
    #     else:
    #         return self.fast(x,n)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 != 0:
            return (x * pow(x, n-1))

        return self.myPow(x,n/2) ** 2