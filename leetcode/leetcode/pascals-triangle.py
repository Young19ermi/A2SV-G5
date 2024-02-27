class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n ==1:
            return [[1]]

        res = [1]
        prev = self.generate(n-1)
        before = prev[-1]

        for i in range(n-2):
            res.append(before[i] + before[i+1])
        
        res.append(1)

        return prev + [res]