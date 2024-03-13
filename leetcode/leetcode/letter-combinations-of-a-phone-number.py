class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
       
        ans=[]
        path=[]
        
            

        def helper(num):
            if len(path)==len(digits):
                
                       
                ans.append(''.join(path[:]))
                
                return
            for i in dict[digits[num]]:
                # if s[i] in dict num and s[i]==s[i-1]:
                #     continue
                 
                    
                 
                    
                    
                path.append(i)
                helper(num+1)
                path.pop()
              
        helper(0) if digits else []
        return ans