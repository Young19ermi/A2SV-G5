class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)

        
        for i in range(len(boxes)):
            p = 0
            for j in range(len(boxes)):
                
                if boxes[j] == "1":
                    p += abs(i-j)
                    
            ans[i]  = p
        return ans
        