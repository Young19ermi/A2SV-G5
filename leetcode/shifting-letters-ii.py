class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        arr = [0 for _ in range(n+1)]
        for l, r, k in shifts:
            if k == 1:
                arr[l] += 1
                arr[r+1] -= 1
            else:
                arr[l] -= 1
                arr[r+1] += 1
        
        res = []
        for i in range(n):
            if i != 0: 
                arr[i] += arr[i - 1]
            new_chr_ascii = (ord(s[i]) - ord("a") + arr[i]) % 26 + ord("a")
            res.append(chr(new_chr_ascii))
        return "".join(res)
        
        # alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
        # numbers = []
        # string = ""
        # for i in range(26):
        #     numbers.append(i)
        # mapped = dict(zip(alphabet,numbers))

        # s_numbers = []
        # prefix_sum = [0] * len(shifts)
        # for char in s:
        #     s_numbers.append(mapped[char])
        # print(s_numbers)

        # for shift in shifts:
        #     for i in range(shift[0],shift[1]+1):
        #         if shift[1] == 1:
        #             s_numbers[i] += shift[2]
        #         else:
        #             s_numbers[i] -= 1
        # for i in range(len(s_numbers)):
        #     x = s_numbers[i]
        #     string += mapped[x % 25]
        # return string

                

