class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows and cols == 0:
            return True
        if cols and rows == 0:
            return True
        for i in range(1, rows):
            for j in range(1, cols):
                
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True




