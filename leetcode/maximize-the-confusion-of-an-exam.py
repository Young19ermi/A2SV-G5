
class Solution:
    def maxConsecutiveAnswers(self, nums: str, k: int) -> int:
        i, j = 0, 0  
        counts = defaultdict(int)  
        max_length = 0  
        max_count = 0  
        for j in range(len(nums)):
            counts[nums[j]] += 1
            max_count = max(max_count, counts[nums[j]])

            while (j - i + 1 - max_count) > k:
                counts[nums[i]] -= 1
                i += 1

            max_length = max(max_length, j - i + 1)

        return max_length
