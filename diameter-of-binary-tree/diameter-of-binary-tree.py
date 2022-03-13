# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        def dfs(rt: TreeNode):
            if rt is None:
                return -1
            l, r = dfs(rt.left) + 1, dfs(rt.right) + 1
            d = l + r
            self.max_d = max(d, self.max_d)
            return max(l, r)
        dfs(root)
        return self.max_d