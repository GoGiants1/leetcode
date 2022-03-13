class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        import math
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        direc = [(1,1), (1,0), (0,1), (-1,1),(-1,0),(0,-1),(1,-1),(-1,-1)]
        
        q = deque()
        q.append((0,0,1))
        
        while q:
            x, y, path = q.popleft()
            if not (0<=x<n and 0<=y<n):
                continue

            if x == y == n-1:
                return path
            
            if grid[x][y] != 0:
                continue
            else:
                grid[x][y] = path
            
            for dx, dy in direc:
                xx = dx+x
                yy = dy+y
                q.append((xx,yy,path+1))
        
        return -1
            
            