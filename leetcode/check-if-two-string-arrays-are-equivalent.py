class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res = ""
        for char in word1:
            res += char
        result = ""
        for char in word2:
            result += char
        if res == result:
            return True
        else:
            return False
