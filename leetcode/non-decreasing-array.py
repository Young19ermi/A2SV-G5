class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        modified = False
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if modified:
                    return False
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                modified = True
        
        return True


        """
        if len(nums) == 2:
            return True
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] < nums[i+1]:
                nums[i+1] = nums[i]
                break
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                if nums[i] < nums[i+2]:
                    nums[i+1] = nums[i]
                    break
            elif nums[i] > nums[i+1]:
                if i>=0 and nums[i-1] > nums[i+1]:
                    nums[i] = nums[i-1]
                    break
                elif i>=0 and nums[i-1] > nums[i]:
                    nums[i-1] = nums[i]
                    break
                elif nums[i] > nums[i-1]:
                    nums[i] = nums[i+1]
                    break
            elif nums[i] < nums[i+1]:
                if nums[i-1] > nums[i+1]:
                    nums[i-1] = nums[i]
                    break
            else:
                if nums[i] > nums[i+1] and nums[i-1] > nums[i+1]:
                    nums[i] = nums[i+1]
                    break


        return True if(nums == sorted(nums)) else False
        
"""