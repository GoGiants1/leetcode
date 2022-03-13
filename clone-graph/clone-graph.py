"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        # value is unique
        # cloned node
        d = {}
        def cloneNode(nd: Node):
            if nd.val in d:
                return d[nd.val]
            new_nd = Node(nd.val)
            d[nd.val] = new_nd
            for i, nei in enumerate(nd.neighbors):
                new_nd.neighbors.append(cloneNode(nei))
            return new_nd
        
        return cloneNode(node)