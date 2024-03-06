# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
#def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #numbers = [i+1 for i in range(n)]
        i = 1
        j = n
       
        while i <= j:
            mid = (i + j)//2

            if guess(mid) == 0:
                return mid

            elif guess(mid) == -1:
                j = mid - 1
                
            else:
                i = mid + 1
                
        return 
        
            # if numbers[mid] == guess(n):
            #     return mid
            # elif guess(n) < numbers[mid]:
            #     i = mid-1
            # else:
            #     j = mid + 1