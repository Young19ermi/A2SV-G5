class Solution(object):
    def shipWithinDays(self, weights, days):
       l = max(weights)
       r = sum(weights)


       while l<r:
           mid=(l+r)//2
           if self.canship(mid,weights,days):
               r=mid
           else:
                l=mid+1
       return r
    def canship(self,limit,weights,days):
            cur=0
            days_taken=1
            for weight in weights:
                cur+=weight
                if cur>limit:
                    days_taken+=1
                    cur=weight
            return days_taken<=days