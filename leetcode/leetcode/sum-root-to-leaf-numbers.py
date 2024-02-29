# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        self.digits = "" 
        def solution(node,digits):
            if node.left is None and node.right is None:
                digits += str(node.val)
                self.res += int(digits)
                self.digits = ""
                return

            if node.left:
                solution(node.left, digits + str(node.val))  
            if node.right:  
                solution(node.right, digits + str(node.val))
            
             
            # return self.res

        solution(root, "")
        return self.res
