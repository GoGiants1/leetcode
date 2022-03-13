# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        @cache
        def dfs(rt: TreeNode, acc: int = 0)->int:
            if rt and rt.left is None and rt.right is None:
                return acc * 10 + rt.val
            out = 0
            if rt.left:
                out += dfs(rt.left, acc * 10 + rt.val)
            if rt.right:
                out += dfs(rt.right, acc * 10 + rt.val)
            
            return out
        
        return dfs(root)