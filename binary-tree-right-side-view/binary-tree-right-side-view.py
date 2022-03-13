# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        q = deque()
        q.append((root, 0))
        while q:
            node, lv = q.popleft()
            if len(out) == lv:
                out.append(node.val)
            else:
                out[lv] = node.val
            
            if node.left:
                q.append((node.left, lv + 1))
            if node.right:
                q.append((node.right, lv + 1))
        
        return out