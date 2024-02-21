class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        g = n - 1
        for i in range(n-2,-1,-1):
            if nums[i] + i >= g:
                g=i
        return g == 0