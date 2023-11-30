class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""

    
        strs.sort()

    
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]

   
        return strs[0]
