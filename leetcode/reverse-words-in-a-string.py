class Solution(object):
    def reverseWords(self, s):
        string = ""
        reverse= list(map(str, s.split()))
        string = " ".join(reverse[::-1])
        return string

       