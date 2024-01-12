class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # if nums == [1] * len(nums):
        #     return len(nums) - 1
        counter = defaultdict(int)
        i = 0
        j = 0
        res = 0
        maximum = 0
        while j < len(nums):
            counter[nums[j]] = 1 + counter.get(nums[j], 0)
            while counter[0] > k and i < len(nums):
                counter[nums[i]] -= 1
                i += 1
                res -= 1
            j += 1
            res += 1
            maximum = max(maximum, res)
        return maximum

        