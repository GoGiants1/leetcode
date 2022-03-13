# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
            root 에서 왼쪽은 pre order, 오른쪽은 post order? 
        """
        def left_tree(rt):
            if rt is None:
                return [None, None]
            l = left_tree(rt.left)
            r = left_tree(rt.right)
            
            return [rt.val, *l, *r]
        
        def right_tree(rt):
            if rt is None:
                return [None,None]

            return [rt.val, *right_tree(rt.right), *right_tree(rt.left)]
        
        
        if left_tree(root.left) == right_tree(root.right):
            return True

        return False