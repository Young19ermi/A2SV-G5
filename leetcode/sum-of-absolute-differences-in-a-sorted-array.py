class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = [0] * len(nums)
        exclusive_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        total = sum(nums)
        left,right = 0,0
        res = []
        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i] 
        j = 0
        n = len(nums)
        res.append(abs((len(nums[1:])*nums[0]) - (total - prefix_sum[0])))
        for i in range(1,len(nums)):
            left = ((i)*nums[i])-prefix_sum[i-1]
            right = abs((n- (i+1))*nums[i] - (total - prefix_sum[i]))
            res.append(left + right)
            left,right = 0,0
        return res









        # prefix_sum = [0] * len(nums)
        # prefix_sum[0] = nums[0]
        # total = sum(nums)
        # left,right = 0,0
        # res = []
        # for i in range(1,len(nums)):
        #     prefix_sum[i] = prefix_sum[i-1] + nums[i]
        # exclusive_sum = [0] * len(nums)
        # for i in range(1,len(nums)):
        #     exclusive_sum[i] = exclusive_sum[i-1] + nums[i-1] 
        # res = []
        # for i in range(len(nums)):
        #     left = (len(nums[:i])*nums[i])-exclusive_sum[i]
        #     right = abs((len(nums[i+1:])*nums[i]) - (total - prefix_sum[i]))
        #     res.append(left + right)
        #     left = 0
        #     right = 0
        # return res









        # prefix_sum = [0] * len(nums)
        # prefix_sum[0] = nums[0]
        # total = sum(nums)
        # left,right = 0,0
        # res = []
        # for i in range(1,len(nums)):
        #     prefix_sum[i] = prefix_sum[i-1] + nums[i]
        # exclusive_sum = [0] * len(nums)
        # for i in range(1,len(nums)):
        #     exclusive_sum[i] = exclusive_sum[i-1] + nums[i-1] 
        # res = []
        # for i in range(len(nums)):
        #     left = (len(nums[:i])*nums[i])-exclusive_sum[i]
        #     right = abs((len(nums[i+1:])*nums[i]) - (total - prefix_sum[i]))
        #     res.append(left + right)
        #     left = 0
        #     right = 0
        # return res


