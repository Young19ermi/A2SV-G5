class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(','}':'{',']':'['}
        for char in s:
            if char in mapping:
                if  stack and mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack                     




        """
        teststring  = list(s)
        stack = []

        def pop(self):
            for i in range(len(teststring)):

                res = self.teststring.pop()

                if res == ')' and teststring[-1] == '(':
                    return True
                return False    
                    
            
                if  res == '}' and teststring[-1] == '{':
                    return True
                return False    
                    
            
                if res == ']' and teststring[-1] == '[':
                    return True

                return False
        """