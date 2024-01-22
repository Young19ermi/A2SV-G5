class Solution(object):
    def balancedString(self, s):
    
        n = len(s)
        count_me = Counter(s)
        
        max_count = n // 4
        
        # Initialize minimum length as the complete string length
        minimum_length = n
        
        i = 0
        counted = Counter()
        
        for j in range(n):
            counted[s[j]] += 1
            
            
            while i < n and all(count - counted[char] <= max_count for char, count in count_me.items()):
                minimum_length = min(minimum_length, j - i + 1)
                counted[s[i]] -= 1
                i += 1
        
        return minimum_length

#         n = len(string)
       
#         countme = Counter(list(string))
#         i = 0
#         counted = 0
#         minimum = 0
#         for j in range(len(string)):
#             while countme[string[j]] >= n//4 and i < len(string):
#                 counted += 1
#             minimum = min(minimum,counted)
#             counted = 0
#             i += 1
#         return minimum
