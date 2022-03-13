# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def findMaxDiff(mx: int, mn: int, now: int):
            a = abs(mx - now)
            b = abs(mn - now)
            return a if a > b else b
            
        
        def traverse(rt: TreeNode | None, mx: int, mn: int ):
            if rt is None:
                return 0
            diff = findMaxDiff(mx,mn, rt.val)
            if rt.val > mx:
                mx = rt.val
            if rt.val < mn:
                mn = rt.val
            l = traverse(rt.left, mx, mn)
            r = traverse(rt.right, mx,mn)
            return max(l,r,diff)
        
        
            
        
        l, r = traverse(root.left, root.val,root.val), traverse(root.right, root.val,root.val)
        
        return max(l,r)
        