class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rottens = deque()
        fresh_oranges = set()
        # find rotten orenge
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rottens.append((r,c, 0))
                elif grid[r][c] == 1:
                    fresh_oranges.add((r,c))
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minute = 0
        while rottens:
            r, c, minute = rottens.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if (nr, nc) in fresh_oranges:
                    rottens.append((nr, nc, minute + 1))
                    fresh_oranges.remove((nr,nc))


        return -1 if len(fresh_oranges) else minute

# 0 <= nr < m and 0 <= nc < n and