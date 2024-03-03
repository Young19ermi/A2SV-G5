# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        def solution(node):
            if node:
                solution(node.left)
                res.append(node.val)
                solution(node.right)
        solution(root)
        start = res.index(low)
        end = res.index(high)
        return sum(res[start:end+1]) if res else 0