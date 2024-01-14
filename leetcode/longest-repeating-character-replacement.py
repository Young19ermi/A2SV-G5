class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        maxf = 0
        l = 0
        for r in range(len(s)):
          dic[s[r]] += 1
          if dic[s[r]] > maxf:
            maxf = dic[s[r]]
          if r - l + 1 - maxf > k:
            dic[s[l]] -= 1
            l += 1
        
        return r - l + 1
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count =  {}
#         left = 0
#         right = 0
#         res = 0
#         maxf = 0
#         while right < len(s):
#             count[s[right]] = 1 + count.get(s[right], 0)
#             while (right - left + 1) - max(count.values()) <= k:
#                 right += 1 
#             count[s[left]] -= 1
#             maxf = max(maxf, right - left + 1)
#             left += 1
#         return maxf
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count =  {}
#         left = 0
#         right = 0
#         res = 0
#         maxf = 0
#         while right < len(s):
#             count[s[right]] = 1 + count.get(s[right], 0)
#             while (right - left + 1) - max(count.values()) > k:
#                 left += 1
#                 count[s[left]] -= 1
#             #right += 1
#             maxf = max(maxf, right - left + 1)
#             right += 1
#         return maxf
# #indices incrementation is always after desired operation