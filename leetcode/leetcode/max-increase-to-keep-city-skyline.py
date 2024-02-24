class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                allowable = min(row_max[row], col_max[col])
                add = allowable - grid[row][col]
                res += add
        return res
