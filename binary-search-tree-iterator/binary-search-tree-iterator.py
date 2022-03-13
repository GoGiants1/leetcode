# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = 0
        self.nums = self.inorder(root)
    def inorder(self, rt: TreeNode | None):
        if rt is None:
            return []
        return self.inorder(rt.left) + [rt.val] + self.inorder(rt.right)


    def next(self) -> int:
        out = self.nums[self.curr]
        self.curr += 1
        return out

    def hasNext(self) -> bool:
        if self.curr < len(self.nums):
            return True
        return False
    

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()