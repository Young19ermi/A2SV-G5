class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
      
        pt = sorted(points, key=lambda x: x[1])
        count = 0
        end = float('-inf')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

        for i in pt:
            if end < i[0]:                
                count += 1
                end = i[1]
                
        return count