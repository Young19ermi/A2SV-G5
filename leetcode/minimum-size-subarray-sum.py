
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Dynamic Sliding Window
        left = 0
        right = 0
        res = float("inf")
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(right-left + 1, res)
                total -= nums[left]
                left+=1
        return 0 if res == float('inf') else res

