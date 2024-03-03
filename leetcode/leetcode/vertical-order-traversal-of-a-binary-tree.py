# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         level = defaultdict(list)
#         def solution(node,row,col):
#             if node:
#                 solution(node.left, row+1, col-1)
#                 solution(node.right, row+1, col+1)
#                 level[(row , col)].append(node.val)
#         solution(root,0,0)
#         sorted_dict = dict(sorted(level.items(), key = lambda x: (x[0][1] , x[0][0])))
#         by_col = defaultdict(list)
#         for key,items in sorted_dict.items():
#             by_col[key[1]].append(items)
#         result_list = []
#         for key, value in by_col.items():
#             if len(value) > 1:
#                 sorted_values = sorted([item for sublist in value for item in sublist])
#                 print(sorted_values)
#                 result_list.append(sorted_values)
#             else:
#                 result_list.append(value[0])
#         return result_list
# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = defaultdict(list)
        
        def solution(node, row, col):
            if node:
                solution(node.left, row + 1, col - 1)
                level[(col, row)].append(node.val)  # Adjusted column and row order
                solution(node.right, row + 1, col + 1)
        
        solution(root, 0, 0)
        
        sorted_dict = dict(sorted(level.items(), key=lambda x: (x[0][0], x[0][1])))
        
        by_col = defaultdict(list)
        for key, items in sorted_dict.items():
            by_col[key[0]].extend(sorted(items))
        
        result_list = []
        for key in sorted(by_col):
            result_list.append(by_col[key])
        
        return result_list
