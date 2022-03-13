class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from functools import cache
        direc = [(0,1),(-1,0) , (1,0), (0, -1)]
        from itertools import product
        self.ROWS = len(board)
        self.COLS = len(board[0])
        borders = [(i, j) for i in range(self.ROWS) for j in (0, self.COLS - 1)] + \
            [(i, j) for i in (0, self.ROWS - 1) for j in range(1, self.COLS -1)]
                
        def dfs(x:int, y:int):
            if not (0 <= x < len(board) and 0 <= y < len(board[0])) or board[x][y] != "O":
                return

            board[x][y] = "E"
            for dx, dy in direc:
                xx, yy = x + dx, y + dy
                dfs(xx, yy)
        for r, c in borders:
            dfs(r, c)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # captured
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # escaped





