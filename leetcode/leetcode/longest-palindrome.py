class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = Counter(s)
        s = s.lower()
        ans = 0
        odd = 0
        for key,items in letters.items():
            if items % 2== 0:
                ans += items
            else:
                ans += items-1
                odd = 1
        return ans + odd