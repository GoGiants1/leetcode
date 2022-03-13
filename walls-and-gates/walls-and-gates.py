class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(pos):
            q = deque()
            q.append((*pos, 0))
            
            while q:
                r, c, dist = q.popleft()
            
                for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                    if 0 <= nr < m and 0 <= nc < n:
                        nei = rooms[nr][nc]
                        if nei > dist + 1:
                            rooms[nr][nc] = dist + 1
                            q.append((nr, nc, dist + 1))
        
        INF = 2 ** 31 - 1
        WALL = -1
        GATE = 0
        m, n = len(rooms), len(rooms[0])
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == GATE:
                    bfs((r,c))

 
