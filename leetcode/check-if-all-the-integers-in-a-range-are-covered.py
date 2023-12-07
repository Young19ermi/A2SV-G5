class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            flag = False
            for l,j in ranges:
                if i in range(l,j+1):

                    flag = True
            if flag == False:
                return False

        return True


#range(l,j+1)

        