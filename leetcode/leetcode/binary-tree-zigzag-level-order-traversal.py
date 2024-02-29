# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        k = defaultdict(list) 
        def solution(node, depth):
            if node:
                solution(node.left, depth + 1) 
                solution(node.right, depth + 1)
                k[depth].append(node.val)
        solution(root, 0)
        res = []
        sorted_dict = dict(sorted(k.items(), key=lambda x: x[0]))
        for key,items in sorted_dict.items():
            if key % 2 != 0:
                res.append(items[::-1])
            else:
                res.append(items)
        return res
