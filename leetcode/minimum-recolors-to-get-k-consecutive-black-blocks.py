class Solution:
    def minimumRecolors(self, string: str, k: int) -> int:
        
        i = 0
        j = 0
        count = 0
        minimum = float("inf")
        while j < len(string):
            if j - i + 1 < k:
                if string[j] == 'W':
                    count += 1
                j += 1
            else:
                if string[j] == 'W':
                    count += 1
                minimum = min(minimum, count)
                if string[i] == 'W':
                    count -= 1
                i += 1
                j += 1
        return minimum

        # i = 0
        # j = 0
        # count = 0
        # minimum = float("inf")
        # while j < len(string):
        #     if j - i + 1 < k:
        #         if string[j] == 'W':
        #             count += 1
        #         j += 1
            
        #     minimum = min(minimum, count)
        #     if string[i] == 'W':
        #         count -= 1
        #     i += 1
        # return minimum

        # i = 0
        # j = 0
        # count = 0
        # minimum = float("inf")
        # while j < len(string):
        #     while j -i + 1 < k:
        #         if string[j] == 'W':
        #             count += 1
        #         j += 1
        #     minimum = min(minimum,count)
        #     if string[i] == 'W':
        #         count -= 1
        #     i += 1
        # return minimum 

