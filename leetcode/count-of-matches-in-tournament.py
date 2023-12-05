class Solution(object):
    def numberOfMatches(self, n):
        """
        ans = 0
        if n % 2 == 0:
            ans += n-1
        else:
            ans += (n - 1) 
        return ans
        #return n-1 if n%2 == 0 else n-1
        n = n-1
        return n
        """
        s=0
        t=n
        m=1
        while(m>0):
            m=t//2
            t=t-m
            s=s+m
        return s
  



        