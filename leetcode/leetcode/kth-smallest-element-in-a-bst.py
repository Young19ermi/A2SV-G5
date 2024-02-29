# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def solution(node):
            if node is not None:
                solution(node.left)
                res.append(node.val)
                solution(node.right)
        solution(root)
        return res[k-1]