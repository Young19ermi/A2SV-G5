class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        nums = str(x)
        for i in range(len(nums)):
            left = 0
            right = len(nums)-1 
            while left < right:
                if nums[right] == nums[left]:
                    left += 1
                    right -= 1
        return True
        """
        nums = str(x)

        rev = nums[::-1]
        if nums == rev:
            return True
        return False


