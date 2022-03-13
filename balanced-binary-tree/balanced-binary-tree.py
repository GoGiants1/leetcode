# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def dfs(rt: TreeNode | None):
            if rt is None:
                return 0
            a = dfs(rt.left)
            if a == -1:
                return -1
            b = dfs(rt.right)
            if b == -1:
                return -1
            if abs(a-b) > 1:
                return -1
            return max(a,b) + 1
        return dfs(root) != -1