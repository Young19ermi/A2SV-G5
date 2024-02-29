class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        TreeNode(val)

        if not node:
            return TreeNode(val)
        
        if val < node.val:
            self.insertIntoBST(node.left,val)
        if val > node.val:
            self.insertIntoBST(node.right,val)

        if node.left is None and val < node.val:
            node.left = TreeNode(val)
        elif node.right is None and val > node.val:
            node.right = TreeNode(val)
        return node



