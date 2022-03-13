class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # Maximum path? 
        # 0 is water, 1 is land in matrix
        # manhattan dist 
        
        # 1. find waters(w) and lands(l)
        # => O(w + l) = O(n**2), w + l = n**2

        # 2. calc nearest land is most far -> O(w*k)
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        
        for r,c in product(range(ROWS), range(COLS)): # prepopulate BFS queue with sources
            if grid[r][c]: queue.append((r,c))

        if not queue or ROWS * COLS == len(queue): # no land or all land
            return -1
        
        visited = set()
        level = 0
        while queue: # count number of BFS layers
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in (0,1),(1,0),(0,-1),(-1,0):
                    nr,nc = r+dr,c+dc
                    if ROWS > nr >= 0 <= nc < COLS and not grid[nr][nc] and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            level += 1
        return level - 1