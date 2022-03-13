"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def buildNode(x: int, y: int, size:int)-> Node:
            if size == 1:
                return Node(val=grid[x][y], isLeaf = True)
            is_leaf = True
            s = 0
            for r in range(x, x + size):
                s += sum(grid[r][y : y + size])
            if not (s == 0 or s == size ** 2):
                is_leaf = False
            
            if is_leaf:
                return Node(val=grid[x][y], isLeaf = True)
            else:
                tl = buildNode(x, y, size // 2)
                tr = buildNode(x, y + size // 2, size // 2)
                bl = buildNode(x + size // 2, y, size // 2)
                br = buildNode(x + size // 2, y + size // 2, size // 2)
                nd = Node(grid[x][y], False , tl, tr, bl, br)
                return nd
        
        return buildNode(0,0, len(grid))


