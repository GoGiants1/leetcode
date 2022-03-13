# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Post Order DFS
        m = - math.inf
        def post_order_DFS(rt: Union[TreeNode | None]) -> int:
            nonlocal m
            if rt is None:
                return 0
            
            l, r = max(post_order_DFS(rt.left), 0),  max(post_order_DFS(rt.right), 0)
            
            m = max(m, l + r + rt.val)
            
            return max(l + rt.val, r + rt.val)
        
        post_order_DFS(root)
        return m