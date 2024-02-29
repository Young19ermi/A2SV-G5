class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val == val:
            return root
        if root and val < root.val:
            return self.searchBST(root.left,val)
        elif root and val > root.val:
            return self.searchBST(root.right,val)