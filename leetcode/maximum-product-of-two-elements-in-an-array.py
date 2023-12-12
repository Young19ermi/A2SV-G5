class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        return (nums[right]-1)*(nums[right-1]-1)
        """
        i = 0
        j = len(nums)-1
        total = 0
        maxtotal = 0
        while i <= len(nums)-1 and j <= len(nums)-1:
            total += (nums[i]-1)*(nums[j]-1)
            maxtotal = max(maxtotal, total)
            total = 0
            i+=1
            j-=1
        return maxtotal
        """
