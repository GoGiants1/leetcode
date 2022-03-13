# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # dfs
        
        def dfs(rt: TreeNode)->list[list[int]]:
            if rt.left is None and rt.right is None:
                return [[rt.val]]
            
            out = []
            if rt.left:
                l = dfs(rt.left)
                out.extend(l)
            if rt.right:
                r = dfs(rt.right)
                out.extend(r)
            
            for p in out:
                p.append(rt.val)
            
            return out
        
        paths = dfs(root)
        
        s = 0
        
        for p in paths:
            for i, v in enumerate(p):
                s += v * pow(10, i)
        
        return s