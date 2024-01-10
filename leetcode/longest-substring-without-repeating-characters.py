class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        letters =set()
        left = 0
        max_length = 0
        for right in range(len(string)):
            while string[right] in letters:
                letters.remove(string[left])
                left += 1
            letters.add(string[right])
            right += 1
            max_length =max(max_length, len(letters))
        return max_length        

       