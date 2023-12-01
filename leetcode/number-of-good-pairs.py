class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = []
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    ans.append([nums[i], nums[j]])
            res.append(ans)
        return len(ans)


        
        