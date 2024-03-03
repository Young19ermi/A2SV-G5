
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # minimum,maximum = float('inf'), 0
        # def solution(node):
        #     nonlocal minimum, maximum
        #     if not node:
        #         return 

        #     minimum = min(minimum,node.val)
        #     maximum = max(maximum,node.val)
          
        #     return solution(node.left) 
        #     return solution(node.right)
            
        # solution(root)
        # return abs(minimum - maximum)

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def solution(node, minimum, maximum):
            if not node:
                return maximum - minimum
                
            minimum = min(minimum,node.val)
            maximum = max(maximum,node.val)
          
            return max(solution(node.left, minimum, maximum), solution(node.right, minimum, maximum))
            
        return solution(root, float('inf'), 0)