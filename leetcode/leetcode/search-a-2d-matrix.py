class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mixed = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mixed.append(matrix[i][j])
        print(mixed)

        i = 0
        j = len(mixed)-1

        while i <= j:
            mid = (i+j) // 2

            if mixed[mid] == target:
                return True
            elif mixed[mid] < target:
                i = mid+1
            else:
                j = mid-1
        return False