class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        time_max = max(piles)
        i = 1
        j = max(piles)

        while i <= j:
            mid = (i + j) // 2
            t = 0
            #print(i,j,mid)
            for k in range(len(piles)):
                if t > h:
                    break
                else:
                    if piles[k] < mid:
                        t += 1
                    else:
                        t += ceil(piles[k] / mid)
                        
            
            if t <= h:

                j = mid-1
            else:
                i = mid +1

        return i

        