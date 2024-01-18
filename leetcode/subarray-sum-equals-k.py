class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = defaultdict(int)
        prefixsum[0] = 1
        res = 0
        total = 0
        for num in nums:
            total += num
            res += prefixsum[total - k]
            prefixsum[total] += 1
        return res