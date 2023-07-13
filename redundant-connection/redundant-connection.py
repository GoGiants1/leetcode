class UnionFind:
    def __init__(self, n:int):
        self.parent = {i: i for i in range(1, n + 1)}
        self.rank = [0] * (n + 1)

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x :int, y: int):
        par_x = self.find(x)
        par_y = self.find(y)

        if par_x == par_y:
            return False
        if self.rank[par_x] < self.rank[par_y]:
            self.parent[par_x] = par_y
        elif self.rank[par_x] > self.rank[par_y]:
            self.parent[par_y] = par_x
        else:
            self.parent[par_y] = par_x
            self.rank[par_x] += 1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        u = UnionFind(len(edges))

        for v, w in edges:
            if not u.union(v, w):
                return [v,w]


            
