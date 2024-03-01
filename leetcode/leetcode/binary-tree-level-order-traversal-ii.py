# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        def solution(node, depth):
            if node:
                solution(node.left, depth + 1)
                solution(node.right, depth + 1)
                levels[depth].append(node.val)
        solution(root, 0)
        res = []
        sorted_dict = dict(sorted(levels.items(), key = lambda x:x[0]))
        for key,items in sorted_dict.items():
            res.append(items)
        return res[::-1]