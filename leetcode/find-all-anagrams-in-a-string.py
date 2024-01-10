class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter

        m,n = len(s),len(p)
        if m < n :
            return []
        s_count = Counter(s[:n])
        p_count = Counter(p)
        res = []

        left,right = 0, n - 1

        while right < m:
            if p_count == s_count:
                res.append(left)
            s_count[s[left]] -= 1 # But this one means just substract the occurence of that element from the entire 

            if s_count[s[left]] == 0:
                del s_count[s[left]] # because delete means removing the char from the entire s_count
            left += 1
            right += 1
            if right < m:
                s_count[s[right]] += 1

                
        return res        