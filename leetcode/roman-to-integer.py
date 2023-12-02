class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        prev_value = 0
        for char in s:
            value = dict[char]
            if value > prev_value:
                res += value - 2 * prev_value
            else:
                res += value
            prev_value = value
        return res



        
