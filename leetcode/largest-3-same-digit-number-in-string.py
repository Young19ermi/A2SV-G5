class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left = 0
        right = 2
        res = []
        ans = ""
        while left < len(num) and right < len(num):
            if num[left] == num[right]:
                if num[left] == num[left + 1]:
                    res.append(num[left])
            left += 1
            right += 1
        if len(res) != 0:
            res = max(res)
            ans = res*3
        return ans







