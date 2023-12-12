class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10 and n % 2 == 0:
            return False
        elif n==1:
            return True

        num = str(n)
        n=0
        for i in range(len(num)):
            n += int(num[i])**2
        return self.isHappy(n)
    






        """
        nums = [int(l) for l in str(n)]
        left = 0
        right = len(nums)-1
        while left <= len(nums)-1 and right <= len(nums)-1:
            if nums[left]**2 + nums[right]**2 != 100 or nums[left]**2 + nums[right]**2 != 10 :
                continue
                left+=1
                right-=1
            return True
        return False
        """

        