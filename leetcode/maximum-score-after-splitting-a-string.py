class Solution:
    def maxScore(self, s: str) -> int:
        nums = list(s)
        l_sum = [0] * len(nums)
        r_sum = [0] * len(nums)
        res= []
        
        for i in range(len(nums)):
            l_sum[i] += nums[:i+1].count(str(0))
        print(l_sum)
            
        nums[::-1]
        for i in range(len(nums)):
            r_sum[i] += nums[i+1:].count(str(1))
        print(r_sum)


        
        for i in range(len(l_sum)-1):
            res.append(l_sum[i] + r_sum[i])
        return max(res)
        