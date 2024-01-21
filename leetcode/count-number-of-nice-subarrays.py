class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        odd_count = 0
        count = 0
        res = 0
        for j in range(len(nums)):
            if nums[j] % 2 != 0:
                odd_count += 1
                count = 0
            while odd_count == k:
                if nums[i] % 2 != 0:
                    odd_count -= 1
                i += 1
                count += 1
                
            res += count
        return res