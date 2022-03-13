# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS, Iteration
        
        from collections import deque
        
        q = deque([(0, root)])
        out = []
        
        while q:
            lvl, node = q.popleft()
            if node:
                if node.left:
                    q.append((lvl + 1, node.left))
                if node.right:
                    q.append((lvl + 1, node.right))

                if lvl < len(out):
                    out[lvl].append(node.val)
                else:
                    out.append([node.val]) 
                
        return out