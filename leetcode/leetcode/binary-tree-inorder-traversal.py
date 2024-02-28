class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def solution(node):
            if node is not None:
                solution(node.left)
                res.append(node.val)
                solution(node.right)
        solution(root)
        return res

