class Solution:
    def firstUniqChar(self, s: str) -> int:
    
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for i, letter in enumerate(s):
            if char_count[letter] == 1:
                return i
        return -1
       

      

        """
        mydict = {}
        res = []
        ans = []
        result = 0
        if len(s) == 1:
            return 0 #if s in mydict and mydict[s] == 1 else -1
        for letter in s:
            if letter in mydict:
                mydict[letter] += 1
            else:
                mydict[letter] = 1
        for item, value in mydict.items():
            if value == 1:
                res.append(item)
        for i in range(len(res)-1):
            if res[i] in s:
                ans.append(s.index(res[i]))
                ans.sort()
        if ans:
            return ans[0] 
        return -1

    
        mydict = {}
        res = []
        ans = []
        result = 0
        if len(s) == 1:
            return 0 
        for letter in s:
            if letter in mydict:
                mydict[letter] += 1
            else:
                mydict[letter] = 1
        for item, value in mydict.items():
            if value == 1:
                res.append(item)
        for i in range(len(res)-1):
            if res[i] in s:
                ans.append(s.index(res[i]))
                ans.sort()
        if ans:
            return ans[0]
        return -1
        """
        
       
 