class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        total = []
        summe = sum(num for num in nums if num % 2 == 0) 
        for operation in queries:
            val, index = operation
            if nums[index] % 2 == 0: 
                if val % 2 == 0:  
                    summe += val  
                else:  
                    summe -= nums[index]  
            else:  
                if val % 2 != 0: 
                    summe += nums[index] + val  
            nums[index] += val 
            total.append(summe)  
        return total

        """
        total = []
        
        for operation in queries:
            
            nums[operation[1]] += operation[0]
            summe = 0
            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    summe += nums[i]
            total.append(summe)

        return total



        total = []
        
        for operation in queries:
            
            nums[operation[1]] += operation[0]
            summe = 0
            for num in nums:
                if num % 2 == 0:
                    summe += num
            total.append(summe)

        return total
        """


        