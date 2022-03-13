# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # divide and conquer
        # inorder -> subtree structure
        # postorder -> root finder in sub_tree
        #My Sol
        def makeTreeNode(in_sub_idx: tuple[int,int], post_sub_idx: tuple[int, int]):
            # print("in", in_sub_idx, "post", post_sub_idx)
            in_start, in_end = in_sub_idx
            post_start, post_end = post_sub_idx
            
            if in_start > in_end or post_start > post_end:
                return None
            
            if in_start == in_end:
                return TreeNode(val=inorder[in_start])
            
            root = TreeNode(postorder[post_end])
            
            in_root_idx = inorder.index(root.val, in_start, in_end + 1)
            
            l_in_idxs = (in_start, in_root_idx - 1)
            r_in_idxs = (in_root_idx + 1, in_end)
            
            l_post_idxs = (post_start, post_start + in_root_idx - in_start - 1)
            r_post_idxs = (post_start + in_root_idx - in_start, post_end -1)
            
            root.left, root.right = makeTreeNode(l_in_idxs, l_post_idxs),  makeTreeNode(r_in_idxs, r_post_idxs)
            
            return root
        return makeTreeNode((0, len(inorder) - 1), (0, len(inorder) - 1))

# Sol from discuss
#         if not inorder:
#             return None
#         cur_val = postorder.pop()
#         idx = inorder.index(cur_val)
#         right = self.buildTree(inorder[idx+1:], postorder)
#         left = self.buildTree(inorder[:idx], postorder)
#         return TreeNode(cur_val, left, right)
            
            
            
                