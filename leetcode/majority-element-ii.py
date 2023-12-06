class Solution(object):
    def majorityElement(self, nums):
        n =len(nums)
        n = (n // 3)
        count = Counter(nums)
        res = []
        for key,value in count.items():
            if value > n:
                res.append(key)
            else:
                continue
        return res
        
