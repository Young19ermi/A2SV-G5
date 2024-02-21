class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = sorted(costs, key = lambda x:x[0]-x[1])
        output = 0
        print(diff)
        for i in range((len(diff)//2)):
            output += diff[i][0]
        for j in range((len(diff)//2),len(diff)):
            output += diff[j][1]
        return output
        # for a,b in costs:
        #     diff.append(a-b)
        # diff.sort()
        # relate = {}
        # for 