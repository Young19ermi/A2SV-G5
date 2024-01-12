class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        m = nums.count(val)
        nums.sort(key =lambda x:x==val)
        print(nums)
        for _ in range(m):
            nums.pop()
        print(nums)
        # #return len(nums)- m
        # j = 0
        # for j in range(len(nums)-1):
        #     if nums[j] == val:
        #         if nums[j+1] != 0:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]
        #         else:
        #             k = 0
        #             if nums[j+k] == val:
        #                 k += 1
        #             else:
        #                 nums[j],nums[j+k] = nums[j+k],nums[j]
        # for _ in range(m):
        #     nums.pop()
        # print(nums)
        # #return len(nums)- m