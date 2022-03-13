# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursive_inorder(root):
            if root is None:
                return None
            
            l = recursive_inorder(root.left)
            r = recursive_inorder(root.right)
            
            
            if l and r:
                return [*l, root.val, *r]
            elif l is None and r:
                return [root.val, *r]
                
            elif r is None and l:
                return [*l, root.val]
            
            else:
                return [root.val]
                
                
        
        return recursive_inorder(root)