# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def solution(node):
            if node is not None:
                solution(node.left)
                arr.append(node.val)
                solution(node.right)
        solution(root)
        
        def bst(arr,l, r):
            if l == r:
                return TreeNode(arr[l])
            if l > r:
                return
            
            mid = l + (r -l) // 2
            root = TreeNode(arr[mid])
            root.left = bst(arr,l, mid - 1)
            root.right = bst(arr,mid + 1, r)
            return root
            
        return bst(arr,0,len(arr)-1)