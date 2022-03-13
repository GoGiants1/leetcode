# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # self.out = math.inf
        # def inorder(rt)-> list[int]:
        #     if rt is None:
        #         return []
        #     if rt.left is None and rt.right is None:
        #         return [rt.val]
            
        #     l = inorder(rt.left)
        #     r = inorder(rt.right)
        #     res = []
        #     if len(l) > 0:
        #         self.out = min(self.out, rt.val - l[-1])
        #         res.append(l[0])
        #     else:
        #         res.append(rt.val)
        #     if len(r) > 0:
        #         self.out = min(self.out, r[0] - rt.val)
        #         res.append(r[-1])
        #     else:
        #         res.append(rt.val)
        #     return res
        # inorder(root)
        # return self.out
        self.minDistance = 1e9
        # Initially, it will be null.
        self.prevNode = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            # Find the difference with the previous value if it is there.
            if self.prevNode is not None:
                self.minDistance = min(self.minDistance, node.val - self.prevNode)
            self.prevNode = node.val
            inorder(node.right)

        inorder(root)
        return self.minDistance