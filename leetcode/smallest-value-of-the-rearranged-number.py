class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            res = ""
            num = abs(num)
            nums = list(map(int, str(num)))
            nums.sort(reverse = True)
            for n in nums:
                res += str(n)
            return int("-" + res)
        nums = list(map(int, list(str(num))))
        result = []
        if 0 not in nums:
            nums.sort()
            result = list(map(str, nums))
            return int("".join(result))
        else:
            nums.sort()
            countzeros = nums.count(0)
            for n in nums:
                if n != 0:
                    result.append(n)
            result= result[:1] + [0] * countzeros + result[1:]
            
            return int("".join(list(map(str, result))))
            
            

      


       
        