class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashed = defaultdict(int)
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        hashed[0] = 1
        total = 0
        count = 0
        if nums == [0] * len(nums) and goal == 0:
            for i in range(len(nums)):
                count += len(nums) - i
            return count
        if nums == [0] * len(nums) and goal != 0:
            return 0
        for i in range(len(nums)):
            total += nums[i]
            count += hashed[total - goal]
            hashed[total] += 1
        return count 

