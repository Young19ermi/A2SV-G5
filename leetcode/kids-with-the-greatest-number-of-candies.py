class Solution (object):
    def kidsWithCandies(self, candles, extra):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        total=0
        ans =[]
        for i in range(len(candles)):
            total = candles[i] +extra 
            
            if total >= max(candles):
        
                ans.append(True) 
            else:
                ans.append(False)
        return ans

