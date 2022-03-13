class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # m * n grid of cells

        m = len(board)
        n = len(board[0])

        st = []
        
        direc = [(1,0), (-1,0), (0,1), (0,-1), (1,1),(1,-1), (-1, -1), (-1, 1)]

        def checkNeighbor(pos: tuple[int, int]):
            live_n = 0
            for dr, dc in direc:
                r = pos[0] + dr
                c = pos[1] + dc
                if 0 <= r < m and 0 <= c < n:
                    live_n += board[r][c]
            
            if board[pos[0]][pos[1]]:
                if live_n < 2 or live_n > 3:
                    st.append((*pos, 0))
            else:
                if live_n == 3:
                    st.append((*pos, 1))
        
        for r in range(m):
            for c in range(n):
                checkNeighbor((r,c))
        
        while st:
            x, y, val = st.pop()
            board[x][y] = val

        