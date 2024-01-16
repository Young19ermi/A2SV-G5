class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * len(nums) 
        prefix_sum[0] = nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]
        return prefix_sum 
