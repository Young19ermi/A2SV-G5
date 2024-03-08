class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        right = len(nums)-1
        count = 0
        mod = (10**9 + 7)
        for i, elem in enumerate(nums):
            while (elem + nums[right]) > target and i <= right:
                right -= 1
            if i <= right:
                count += (2 ** (right - i))
                count %= mod
        return count
            

        


































        # nums.sort()
        # count = 0
        # left,right = 0, len(nums)-1
        # res = []
        # while left <= right:
        #     if nums[left] + nums[right] == target:
        #         res.append((left,right))
            
        #         break
        #     elif nums[left] + nums[right] < target:
        #         left += 1
        #     else:
        #         right -= 1
        # print(left,right)
        # before = right - 1
        # after = right
        # while before >= 0 and after > 0:
        #     if nums[before] + nums[after] <= target:
        #         count += 1
        #     after -= 1
        #     before -= 1

        # i,j = left,right
        # while i <= j:
        #     if nums[i] + nums[j] <= target:
        #         count += 1
        #     j-=1
        # return counthh
