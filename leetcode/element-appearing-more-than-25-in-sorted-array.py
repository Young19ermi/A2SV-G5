class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        measure = len(arr) / 4 # 25 % means n/4
        sorted = {}
        output = 0
        for num in arr:
            if num in sorted:
                sorted[num] += 1
            else:
                sorted[num] = 1

        for item,count in sorted.items():
            if count > measure:
                output += item
            else:
                continue
        return output



        