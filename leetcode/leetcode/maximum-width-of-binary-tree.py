class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # m = defaultdict(list)
        # val = 0
        # def dfs(node,depth,v):
        #     if node.left:
        #         dfs(node.left,depth+1,val)
        #         v = 2*val + 1 
        #         m[depth].append(v)
        #     if node.right:
        #         dfs(node.right,depth+1,val)
        #         v = 2*val + 2
        #         m[depth].append(v)
        # dfs(root,0,0)
        # p = max(m.keys())
        # return max(m[p]) - min(m[p]) + 1

        m = defaultdict(list)

   
        def dfs(node,depth,val):
            
            if node and node.left:
                k = (val*2) + 1
                m[depth].append(k)
                dfs(node.left, depth+1, k)
            if node and node.right:
                k = (val * 2) + 2
                m[depth].append(k)
                dfs(node.right, depth +1, k)

        dfs(root,1,0)
        res = 1
        for v in m.values():
            r = max(v) - min(v) + 1
            res = max(res,r)
        return res