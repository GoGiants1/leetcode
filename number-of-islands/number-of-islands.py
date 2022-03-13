class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        visited = set()
        direc = [(1,0), (0,1), (-1,0), (0,-1)]
        cnt = 0

        def bfs(x:int, y:int):
            q = deque()
            q.append((x,y))
            while q:
                x, y = q.popleft()
                for dx, dy in direc:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]) and (xx,yy) not in visited:
                        if grid[xx][yy] == "1":
                            q.append((xx,yy))
                        visited.add((xx,yy))
            return 1
        
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if el == "1" and (i, j) not in visited:
                    cnt += bfs(i,j)
        return cnt