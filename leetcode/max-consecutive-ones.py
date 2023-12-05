class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        left, count = 0, 0
        max_count = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
