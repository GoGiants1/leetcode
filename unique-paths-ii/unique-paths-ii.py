class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def path_through(x:int, y:int)->int:
            if grid[x][y] == 1:
                return 0
            if (x, y) == (m -1, n - 1):
                if grid[x][y] == 0:
                    return 1
            out = 0
            for nr, nc in [(x + 1, y), (x, y + 1)]:
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                    out += path_through(nr, nc)

            return out
    
        return path_through(0,0)