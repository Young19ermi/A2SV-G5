class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sums = 0
        left_sum = 0
        right_sum = 0
        for i in range(len(nums)):
            left_sum += sum(nums[0:i])
            right_sum += sum(nums[i+1:len(nums)])  
            if left_sum == right_sum:
                return i
            left_sum = 0
            right_sum = 0
            
        return -1 
            
        



        


        

        
        

        


        