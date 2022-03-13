class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set() # store visited coordinates
        direc = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def dfs(r:int, c:int)->int:
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] == 0:
                return 0
            out = 0
            visit.add((r,c))
            for dr, dc in direc:
                rr, cc = r+ dr, c + dc
                if (rr, cc) not in visit:
                    out += dfs(r+ dr, c + dc)
            return out + 1
        mx = 0
        for x in range(m):
            for y in range(n):
                if (x,y) not in visit:
                    mx = max(mx, dfs(x,y))
        return mx