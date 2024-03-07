# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # ans = -1
        # low = 0
        # high = n-1

        # while (low <= high):

        #     mid = low + ((high - low + 1) // 2)

        #     if isBadVersion(mid) == 'False':
                
        #         low = mid + 1

        #     elif isBadVersion(mid) == 'True':
        #         ans = mid
        #         high = mid - 1

        # return ans

        l,r=0,n
        while l+1 < r :
            mid=(l+r)//2
            if isBadVersion(mid) :
                r=mid
            else:
                l=mid 
        return r 