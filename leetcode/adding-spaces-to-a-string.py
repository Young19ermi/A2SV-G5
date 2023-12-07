class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        current = 0
        for i, char in enumerate(s):
            if current < len(spaces) and i == spaces[current]:
                res += ' '
                current += 1
            res += char
        return res        



        """j=0
        res=''
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                res += ""
                j += 1
            res += s[i]
        return res   


        i = 0
        j = 0
        count = 0
        res = ''
        x = spaces.split()
        for i in range(len(s)):
            while i < x:
                if i < spaces:
                    i += 1
                elif i == spaces:
                    res += s[:i]
                    res += ' '
                else:
                    break
        return res            

        """
