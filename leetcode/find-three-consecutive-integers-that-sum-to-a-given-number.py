class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res= []
        if num % 3 != 0:
            return []
        div = num // 3
        res.append(div-1)
        res.append(div)
        res.append(div+1)
        return res

		
		
        
        