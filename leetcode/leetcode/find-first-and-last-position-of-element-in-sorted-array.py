class Solution(object):
    def searchRange(self, nums, target):
      left=-1
      right=-1
      for i in range(len(nums)):
          if nums[i]==target:
            left=i
            break
      if left==-1:
          return [-1,-1]
      for i in range(len(nums)-1,left-1,-1):
          if nums[i]==target:
              right = i
              break
      return [left,right]               

