# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def checkRange(n: int):
            if low <= n <= high:
                return True
            return False
        
        def inOrderTraverse(rt: Union[None, TreeNode]) -> int:
            if rt is None:
                return 0
            
            
            s = rt.val if checkRange(rt.val) else 0
            
            l, r = inOrderTraverse(rt.left), inOrderTraverse(rt.right)
            s += l + r
            return s
        
        return inOrderTraverse(root)