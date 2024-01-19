class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n, l, curr_sum = len(nums), 0, 0
        sub_arr = defaultdict(int)
        max_sum = 0
        for r in range(n):
            while sub_arr[nums[r]] > 0:
                sub_arr[nums[l]] -= 1
                curr_sum -= nums[l]
                l += 1

            sub_arr[nums[r]] += 1
            curr_sum += nums[r]
            max_sum = max(max_sum, curr_sum)

            
        return max_sum
        