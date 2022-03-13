# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l_q, r_q = deque(), deque()
        l_q.append(root.left)
        r_q.append(root.right)
        
        while l_q and r_q:
            l, r = l_q.popleft(), r_q.popleft()
            if not (l and r) or l.val != r.val:
                if l is None and r is None:
                    continue
                return False
            l_q.append(l.left)
            l_q.append(l.right)
            r_q.append(r.right)
            r_q.append(r.left)

        return True if not(l_q and r_q) else False


            