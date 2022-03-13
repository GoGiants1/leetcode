# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # preorder
        if root is None:
            return []
        
        dq = deque()
        dq.append((root, 0))
        out = defaultdict(deque)
        
        while dq:
            rt, depth = dq.popleft()
            if depth % 2 == 0:
                out[depth].append(rt.val)
            else:
                out[depth].appendleft(rt.val)
            
            if rt.left:
                dq.append((rt.left, depth + 1))
            if rt.right:
                dq.append((rt.right, depth + 1))
        out_list = []
        for i in range(len(out)):
            out_list.append(list(out[i]))
            
        return out_list
        