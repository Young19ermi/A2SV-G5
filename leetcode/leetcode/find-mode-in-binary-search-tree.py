class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root.val == 0:
            return [0]
        res = []
        def solution(node):
            if node:
                res.append(node.val)
                solution(node.left)
                solution(node.right)
        solution(root)
        count = Counter(res)
        print(count)
        max_count = max(count.values())
        res = []
        for key,items in count.items():
            if items == max_count:
                res.append(key)
        # else:
        #     res.append(0)
        return res

        