# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         if nums == [1] * len(nums):
#             return len(nums) - 1
#         counter = defaultdict(int)
#         i = 0
#         j = 0
#         res = 0
#         maximum = 0
#         while j < len(nums):
#             counter[nums[j]] = 1 + counter.get(nums[j], 0)
#             while counter[0] > 0 and i < len(nums):
#                 i += 1
#                 res -= 1
#                 counter[nums[i]] -= 1
#             j += 1
#             res += 1
#             maximum = max(maximum, res)
#         return maximum
from collections import defaultdict
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums == [1] * len(nums):
            return len(nums) - 1
        counter = defaultdict(int)
        i = 0
        j = 0
        res = 0
        maximum = 0
        while j < len(nums):
            counter[nums[j]] = 1 + counter.get(nums[j], 0)
            # Check if the current element is 0 and update the counter
            while counter[0] > 1 and i < len(nums):
                counter[nums[i]] -= 1
                i += 1
                res -= 1
            j += 1
            res += 1
            maximum = max(maximum, res-1)
        return maximum
