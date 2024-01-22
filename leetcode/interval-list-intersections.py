class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i,j=0,0
        ans=[]
        while i<len(firstList) and j<len(secondList):
            if firstList[i][0]>secondList[j][1]:
                j+=1
            elif secondList[j][0]>firstList[i][1]:
                i+=1
            else:
                x=max(secondList[j][0],firstList[i][0])
                y=min(secondList[j][1],firstList[i][1])
                ans.append([x,y])
                if firstList[i][1] <= secondList[j][1]:
                    i += 1
                else:
                    j += 1
        return ans