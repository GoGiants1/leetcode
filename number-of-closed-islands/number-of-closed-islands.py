class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # # BFS ? Multi source

        # r, c = len(grid), len(grid[0])
        # direction = [(0, -1), (-1,0), (0, 1), (1, 0)]
        # # conn = defaultdict(set)

        # def checkMargin(row, col):
        #     if row == 0 or col == 0 or row == r - 1 or col == c - 1:
        #         return True
        #     else:
        #         return False

        # def bfs(i, j):
        #     is_land = True
        #     lands = deque()
        #     lands.append((i,j))
        #     while lands:
        #         x, y = lands.popleft()
                
        #         if grid[x][y] == 1:
        #             return False
            
        #         if checkMargin(x, y):
        #             if grid[x][y] == 1:
        #                 continue
        #             else:
        #                 is_land = False
        #                 grid[x][y] = -1
        #         else:
        #             grid[x][y] = -1
                
                
        #         for dx, dy in direction:
        #             row = x + dx
        #             col = y + dy
        #             if 0 <= row < r and 0 <= col < c:
        #                 if grid[row][col] == 0:
        #                     lands.append((row, col))
        
        #     return is_land

        # out = 0

        # for i in range(1, r):
        #     for j in range(1, c):
        #         if grid[i][j] == 0:
        #             if bfs(i, j):
        #                 out += 1
        
        # return out

        # Sol 2. DFS

        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1 # mark as visited
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            return left and right and up and down
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and dfs(i, j):
                    count += 1
        
        return count
            
            