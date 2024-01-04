# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         n = len(board)
#         for rows in range(n):
#             elements = set()
#             for cols  in range(n):
#                 if board[rows][cols].isdigit() and board[rows][cols] in elements:
#                     if list(board[:2][:2]) == "." * 3:
#                         return False
#                 else:
#                     elements.add(board[rows][cols])
                    
#         for cols in range(n):
#             elements = set()
#             for rows in range(n):
#                 if board[rows][cols].isdigit() and board[rows][cols] in elements:
#                     if list(board[:2][:2]) == "." * 3:
#                         return False
#                 else:
#                     elements.add(board[rows][cols])
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        # Check rows
        for row in range(n):
            elements = set()
            for col in range(n):
                if board[row][col].isdigit() and board[row][col] in elements:
                    return False
                else:
                    elements.add(board[row][col])
        
        # Check columns
        for col in range(n):
            elements = set()
            for row in range(n):
                if board[row][col].isdigit() and board[row][col] in elements:
                    return False
                else:
                    elements.add(board[row][col])

        # Check 3x3 subgrids
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                elements = set()
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        if board[row][col].isdigit() and board[row][col] in elements:
                            return False
                        else:
                            elements.add(board[row][col])

        return True

        