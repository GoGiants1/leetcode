"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        prev = {}

        q = deque()
        q.append((root, 0))

        while q:
            node, lv = q.popleft()

            if lv in prev:
                prev[lv].next = node
            prev[lv] = node
            
            if node.left:
                q.append((node.left, lv +1))
            if node.right:
                q.append((node.right, lv +1))
            
        return root