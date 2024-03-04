class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=[]
        res=[]
        def sub(i):
            if i>=len(nums):
                res.append(subsets.copy())
                return 
            subsets.append(nums[i])
            sub(i+1)
            subsets.pop()
            sub(i+1)
        sub(0)
        return res
        