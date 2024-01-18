class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pass_count = [0] * 1001
        for trip in trips:
            pass_count[trip[1]] += trip[0]
            pass_count[trip[2]] -= trip[0]

        prefix_sum= [0] *1001
        prefix_sum[0] = pass_count[0]
        for i in range(1, len(pass_count)):
                prefix_sum[i] = prefix_sum[i-1] + pass_count[i]
        for count in prefix_sum:
            if count > capacity:
                return False
        return True
