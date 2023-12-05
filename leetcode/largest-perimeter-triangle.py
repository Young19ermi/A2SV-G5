class Solution(object):
    def largestPerimeter(self, num):
        

        max_perimeter = 0
        n = len(num)
        num.sort(reverse=True)
        for i in range(n-2):
            if num[i] < num[i+1] + num[i+2]:
                max_perimeter = num[i] + num[i+1] + num[i+2]
                break
        return max_perimeter

                



