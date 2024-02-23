class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        index = dict((t,i) for i, t in enumerate(temperatures))
        print(index)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = i - last 
            stack.append(i)
        return res