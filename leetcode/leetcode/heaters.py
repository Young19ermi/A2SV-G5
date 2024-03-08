class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        heaters.sort()
        maxi=float("-inf")
        for i in range(len(houses)):
            l=-1
            r=len(heaters)-1
            while l+1<r:
                mid=(l+r)//2
                if r==0:
                    radius=0
                    break 
                elif houses[i]>=heaters[mid]:
                    radius=min(abs(houses[i]-heaters[r]),abs(houses[i]-heaters[r-1]))
                    l=mid
                elif houses[i]<heaters[mid]:
                    radius=min(abs(houses[i]-heaters[r]),abs(houses[i]-heaters[r-1]))
                    r=mid 
            radius=min(abs(houses[i]-heaters[r]),abs(houses[i]-heaters[r-1]))
            maxi=max(maxi,radius)   
                   
        return maxi
        