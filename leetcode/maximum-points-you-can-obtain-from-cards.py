class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        this = sum(nums[:k])
        i ,j = k-1, len(nums)-1
        winner = this
        while i >= 0:
            this-=nums[i]
            i-=1
            this+= nums[j]
            j-=1
            winner = max(winner, this)
        return winner
 
