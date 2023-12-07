class Solution(object):
    def pivotArray(self, nums, pivot):
        res =[]
        for i in range(len(nums)):
            if nums[i] < pivot:
                res.append(nums[i])
            if nums[i] == pivot:
                continue 
                
        x = nums.count(pivot)
        for _ in range(x):
            res.append(pivot)
   
        for j in range(len(nums)):
            if nums[j] > pivot:
                res.append(nums[j])
        return res
"""
        def pivotArray(self, nums, pivot):
        res =[]
        for i in range(len(nums)):
            if nums[i] < pivot:
                res.append(nums[i])  # Added closing parenthesis
            if nums[i] == pivot:
                continue 
        x = nums.count(pivot)
        for _ in range(x):
            res.append(pivot)
        for j in range(len(nums)):
            if nums[j] > pivot:  # Changed "num" to "nums"
                res.append(nums[j])  # Changed "i" to "j"
        return res  # Added closing parenthesis
        """
