# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def traverse(rt: TreeNode| None, p_v: int, q_v: int)-> TreeNode | None:
            if rt is None:
                return None
            
        
            l = traverse(rt.left, p_v, q_v)
            r = traverse(rt.right, p_v, q_v)
            
            if l and r or rt.val == p_v or rt.val == q_v:
                return rt
            else:
                if l:
                    return l
                else:
                    return r
        
        return traverse(root, p.val, q.val)