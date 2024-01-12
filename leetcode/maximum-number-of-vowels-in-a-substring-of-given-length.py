class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        maximum = 0
        i = 0
        j = k - 1
        
        for idx in range(k):
            if s[idx] in vowels:
                count += 1
        maximum = count
        
        while j < len(s) - 1:
            j += 1
            if s[j] in vowels:
                count += 1
            if s[i] in vowels:
                count -= 1
            i += 1
            maximum = max(count, maximum)
        return maximum







# vowels = set(['a', 'e', 'i', 'o','u'])
#         count = 0
#         maximum = 0
#         i = 0
#         j = 0
#         #for j in range(k):
#         while j < k:
#             if s[j] in vowels:
#                 count += 1
#                 j += 1
#             else:
#                 j += 1
#         maximum = max(maximum ,count)
#         if s[i] in vowels:
#             count -= 1
#         i += 1
#         j += 1
#         return maximum