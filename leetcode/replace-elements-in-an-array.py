class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        num_dict = {num: i for i, num in enumerate(nums)}
        
        for operation in operations:
            if operation[0] in num_dict:
                index = num_dict[operation[0]]
                nums[index] = operation[1]
                del num_dict[operation[0]]
                num_dict[operation[1]] = index
        
        return nums


        """
        d = {num:index for index, num in enumerate(nums)}
        

        for operation in operations:
            if operations[0] in d:
                i = d[operations[0]]
                nums[i] == operations[1]
                del d[operations[0]]
                d[operation[1]] = i
        return nums

        
    
    for operation in operations:
        if operation[0] in num_dict:
            index = num_dict[operation[0]]
            nums[index] = operation[1]
            del num_dict[operation[0]]
            num_dict[operation[1]] = index
    
    return nums




                




                
        



        
        for operation in operations:
            for i in range(len(nums)):
                if nums[i] == operation[0]:
                    nums[i] = operation[1]
        return nums 


       res = []
        i = j = 0
        n =len(nums)
        while i < n and j <= len(operations):
            if nums[i] == operations[j][0]:
                nums[i] = operations[j][1]
                res.append(nums[i])
                i+=1
                j+=1
            else:
                i+=1
        return res            
        """
    
