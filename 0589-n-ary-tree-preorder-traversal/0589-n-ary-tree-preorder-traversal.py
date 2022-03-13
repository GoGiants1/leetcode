"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Recursion
#         out = []
#         if root is None:
#             return out
        
#         out.append(root.val)
#         for i, c in enumerate(root.children):
#             if c is not None:
#                 out.extend(self.preorder(c))
            
        
#         return out
        
        # iteration
        
        stack = [root]
        visit = []
        while stack:
            node = stack.pop()
            if node is not None:
                for i, v in enumerate(reversed(node.children)):
                    stack.append(v)

                visit.append(node.val)
        
        return visit
        
        
            
            
        
        