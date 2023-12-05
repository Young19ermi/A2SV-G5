class Solution(object):
    def decompressRLElist(self, nums):
        res =[]
        ans = []
        for i in range(0 ,len(nums)-1 ,2):
            #res.extend([nums[i] * [nums[i+1]]])
            res.extend([nums[i+1]] * nums[i])

        return res
        """
        for i in range(0, len(nums), 2):
            result.extend([nums[i+1]] * nums[i])
        return result
        """





            


