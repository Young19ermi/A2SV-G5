class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        res = [0] * len(nums)
        
        if 0 in nums:
            indx = nums.index(0)
            nums.remove(0)
            for i in range(len(nums)):
                total *= nums[i]
            res[indx] += total 
            return res
        
           
        else:
            for i in range(len(nums)):
                total *= nums[i]
            for i in range(len(nums)):
                res[i] += total // nums[i]
                print(total)
            return res
