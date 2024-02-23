from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five = 0 
        count_ten = 0

        for n in bills:
            if n ==5:
                count_five += 1
            
            elif n == 10:
                if count_five >= 1:
                    count_ten += 1
                    count_five -= 1
                else:
                    return False
                    

            else:
                if count_ten >= 1 and count_five >= 1:
                    count_five -= 1
                    count_ten -= 1
                elif count_five >= 3:
                    count_five -= 3
                else:
                    return False
        
        return True

