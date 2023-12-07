class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        missingnumber=n
        for i in range(n):
            missingnumber^=i^nums[i]
        return missingnumber

        
        