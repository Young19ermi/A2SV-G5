class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, nums):
            if not nums:
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(path, nums[:i] + nums[i+1:])
                path.pop()

        backtrack([], nums)
        return res
