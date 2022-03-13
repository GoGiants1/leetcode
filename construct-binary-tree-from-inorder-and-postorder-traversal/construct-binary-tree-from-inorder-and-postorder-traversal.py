# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {}
        for i, v in enumerate(inorder):
            inorder_idx[v] = i
        @cache
        def buildT(i_l, i_r, p_l, p_r):
            if i_l > i_r:
                return None
            new_rt = TreeNode(val=postorder[p_r])
            rt_inorder = inorder_idx[new_rt.val]
            
            new_rt.left = buildT(i_l, rt_inorder -1, p_l, p_l + (rt_inorder - i_l) -1)
            new_rt.right = buildT(rt_inorder + 1, i_r, p_l + (rt_inorder - i_l), p_r - 1)
            return new_rt
        
        return buildT(0, len(inorder) - 1, 0, len(inorder) - 1)