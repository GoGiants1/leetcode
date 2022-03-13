# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = -math.inf
        def pathSum(rt: TreeNode | None):
            if rt is None:
                return 0

            me = rt.val
            l = max(pathSum(rt.left), 0)
            r = max(pathSum(rt.right),0)
            self.mx = max(self.mx, me, me+l+r)
            return max(me, l + me, r + me) 

        return max(pathSum(root), self.mx)
        # left, right, left + right 중 max 리턴