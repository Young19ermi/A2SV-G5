class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        letters = list(string.ascii_lowercase)
        numbers = list(range(0,27))
        pairs = dict(zip(letters,numbers))
        l= list(palindrome)
        a = 0
        changed = 0
        if len(palindrome) == 1:
            return ""
        for i in range((len(l)//2)):
            if pairs[l[i]] > pairs['a']:
                l[i] = 'a'
                break
        else:
            l[-1] = 'b'
        return "".join(l)