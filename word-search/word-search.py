class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        direc = [(1,0), (0, 1), (-1, 0), (0, -1)]
        def valid(x, y):
            return 0 <= x < m and 0 <= y < n
        self.out = False
        def backtrack(curr: int, pos: list[int], visited: set):
            x, y = pos
            if  len(visited) == len(word):
                self.out = True
                return
            
            for dx, dy in direc:
                xx, yy = x + dx, y + dy
                if valid(xx,yy) and (xx, yy) not in visited and board[xx][yy] == word[curr]:
                    visited.add((xx, yy))
                    backtrack(curr + 1, [xx, yy], visited)
                    visited.remove((xx,yy))
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    v = set()
                    v.add((i,j))
                    backtrack(1, [i,j], v)
                
        return self.out

            