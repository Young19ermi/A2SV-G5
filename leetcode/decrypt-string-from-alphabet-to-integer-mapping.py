class Solution:
    def freqAlphabets(self, s: str) -> str:
    
        result = ""
        i = len(s) - 1
        
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                result = chr(96 + num) + result
                i -= 3
            else:
                result = chr(96 + int(s[i])) + result
                i -= 1
        
        return result



                

                