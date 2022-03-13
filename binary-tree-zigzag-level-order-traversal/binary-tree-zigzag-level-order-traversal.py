# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out = []
        q = [(root, 0)]
        nxt_lv = []
        while q or nxt_lv:
            if not q:
                q = nxt_lv
                nxt_lv = []
                continue
            node, lv = q.pop()

            if node is None:
                continue
            
            if len(out) == lv:
                out.append([node.val])
            else:
                out[lv].append(node.val)
            
            if lv % 2:
                nxt_lv.append((node.right, lv + 1))
                nxt_lv.append((node.left, lv + 1))
            else:
                nxt_lv.append((node.left, lv + 1))
                nxt_lv.append((node.right, lv + 1))
        return out