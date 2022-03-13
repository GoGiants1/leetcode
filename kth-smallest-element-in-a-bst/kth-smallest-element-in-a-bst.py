# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.out = None
        # def inorder(rt: TreeNode | None, cnt = 0):
        #     if rt is None:
        #         return cnt
        #     l = inorder(rt.left, cnt)
        #     if l is None:
        #         return
        #     cnt = l + 1
        #     if cnt == k:
        #         self.out = rt.val
        #         return
        #     r = inorder(rt.right, cnt)
        #     return r
        # inorder(root)
        # return self.out
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right