class Solution(object):
    def findWords(self, word):
        rows1 = "qwertyuiopQWERTYUIOP"
        rows2 = "asdfghjklASDFGHJKL"
        rows3 = "zxcvbnmZXCVBNM"
        res = []

        for i in range(len(word)):
            x =set()
            for j in range(len(word[i])):
                if word[i][j] in rows1:
                    x.add(1)
                elif word[i][j] in rows2:
                    x.add(2)
                else:
                    x.add(3)
            print(x)
            if len(x) == 1:
                res.append(word[i])
        return res
        