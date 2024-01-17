class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        rows,cols=len(matrix),len(matrix[0])
        self.prefixsum=[[0]*(cols+1) for i in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                self.prefixsum[i+1][j+1] = matrix[i][j] + self.prefixsum[i][j+1] + self.prefixsum[i+1][j] - self.prefixsum[i][j]
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.prefixsum[r2+1][c2+1] - self.prefixsum[r2+1][c1] - self.prefixsum[r1][c2+1] + self.prefixsum[r1][c1]

       