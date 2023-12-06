class Solution(object):
    def shuffle(self, nums, n):
        """
        halflist1 = list[:len(nums)/2]
        halflist2 = list[len(nums)/2:]
        ans = []
        ans.extend()
        """
        x = 0
        res = []
        x = 0
        y = n
        while x < len(nums)//2 and y < len(nums):
            res.append(nums[x])
            res.append(nums[y])
            x+=1
            y+=1
        while x<len(nums) and y<len(nums):
            x+=1
            y+=1
        return res
        


