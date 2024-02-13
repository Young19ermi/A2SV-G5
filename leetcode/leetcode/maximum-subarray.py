class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # i = 0
        # if len(nums) == 1:
        #     return nums[i]
        # else:
        #     prefix_sum = [0] * len(nums)
        #     prefix_sum[0] = nums[0]
        #     for i in range(1,len(nums)):
        #         prefix_sum[i] = prefix_sum[i-1] + nums[i]
        #     minimum = min(prefix_sum)
        #     maximum = max(prefix_sum)
        #     if maximum - minimum < maximum:
        #         return maximum
        #     else:
        #         return maximum - minimum
        # prefix_sum = [0] * len(nums)
        # prefix_sum[0] = nums[0]
        # for i in range(1,len(nums)):
        #     prefix_sum[i] = prefix_sum[i-1] + nums[i]
        # print(prefix_sum)
       # so_far = 0
        total = 0
        so_far = -float("inf")
        for i in range(len(nums)):
            total += nums[i]
            if so_far < total:
                so_far = total
            if total < 0:
                total = 0
        return so_far

#         Initialize:
#     max_so_far = INT_MIN
#     max_ending_here = 0

# Loop for each element of the array

#   (a) max_ending_here = max_ending_here + a[i]
#   (b) if(max_so_far < max_ending_here)
#             max_so_far = max_ending_here
#   (c) if(max_ending_here < 0)
#             max_ending_here = 0
# return max_so_far
        