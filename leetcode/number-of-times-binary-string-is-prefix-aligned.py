# class Solution:
#     def numTimesAllBlue(self, flips: List[int]) -> int:
#         n = len(flips)
#         count = 0
#         bulbs = [0] * (n+1)
#         for i in range(1,n):
#             bulbs[flips[i]] = 1
#             if all(bulbs[1:i]):
#                 count += 1
#         return count
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_index = 0

        for i, bulb in enumerate(flips, 1):
            max_index = max(max_index, bulb)
            if max_index == i:
                count += 1

        return count

        # n = len(flips)
        # bulbs= [0] * n
        # count = 0
        # i = 0
        # while i <= len(flips)-1:
        #     bulbs[flips[i]-1] = 1
        #     if all(bulbs[0:i+1]) == 1: #why i + 1  
        #         count += 1
        #     i+=1
        # return count



