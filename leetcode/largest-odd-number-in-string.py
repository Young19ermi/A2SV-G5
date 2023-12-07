class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        if int(num[-1]) % 2 != 0:
            return num

        largest_odd = ""
        for i in range(len(num)-1):
            if int(num[i]) % 2 != 0:
                largest_odd += num[i]
                if int(num[i+1]) % 2 ==0 and int(num[i+2]) % 2 !=0:
                    largest_odd += num[i+1]
                    largest_odd += num[i+2]
            if int(num[i+1]) % 2 != 0:
                largest_odd += digit
        if largest_odd == "":
            return ""
        else:
            return largest_odd
        """

        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""
