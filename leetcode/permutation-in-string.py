class Solution(object):
    def checkInclusion(self, s1,s2):
        if len(s1) > len(s2):
            return False
    
        s1_map = [0] * 26
        s2_map = [0] * 26
    
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
    
        for i in range(len(s2) - len(s1)):
            if s1_map == s2_map:
                return True
        
            s2_map[ord(s2[i]) - ord('a')] -= 1
            s2_map[ord(s2[i + len(s1)]) - ord('a')] += 1
    
        return s1_map == s2_map
