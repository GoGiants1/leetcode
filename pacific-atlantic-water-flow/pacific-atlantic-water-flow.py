class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs ?

        m, n = len(heights), len(heights[0])

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m)]

        pacific_source = set()
        atlantic_source = set()

        def bfs(start: list, sources: set()):
            q = deque(start)
            seen = set()
            while q:
                r, c = q.popleft()
                for nr, nc in [(r + 1, c), (r, c + 1), (r-1, c), (r, c - 1)]:
                    if (nr, nc) not in seen and 0 <= nr < m and 0 <= nc < n and heights[r][c] <= heights[nr][nc]:
                        q.append((nr, nc))
                        seen.add((nr, nc))
                sources.add((r,c))
        bfs(pacific, pacific_source)
        bfs(atlantic, atlantic_source)
        return pacific_source.intersection(atlantic_source)


        