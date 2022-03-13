class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x: int, y: int):
            cnt = 0
            if x < 0 or x >= m or y < 0 or y >= n:
                return False, 0
            if grid[x][y] == 0:
                return True, 0
            else:
                grid[x][y] = 0
                if 0 < x < m and 0 < y < n:
                    cnt += 1
            
            out = True
            for dx, dy in directions:
    
                is_closed, child_cnt = dfs(x + dx, y + dy)
                cnt += child_cnt
                out &= is_closed
            
            if out is False:
                cnt = 0
            return out, cnt

        ans = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 1:
                    is_closed, cnt = dfs(i, j)
                    if is_closed:
                        ans += cnt

        return ans
