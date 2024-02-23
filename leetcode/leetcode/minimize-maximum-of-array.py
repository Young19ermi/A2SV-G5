class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s = 0
        avg=0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            avg = math.ceil(s/(i+1))
            res = max(res,avg)
            # if avg > s:
            #     s = avg
        return res