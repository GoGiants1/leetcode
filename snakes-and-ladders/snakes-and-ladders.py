class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n ** 2
        @cache
        def int_to_pos(i: int):
            r = (n - 1) - (i - 1) // n
            c = (i - 1) % n if (n - 1 - r) % 2 == 0 else n - 1 - (i - 1) % n
            return r, c
        
        # prev, curr, moves
        q = deque()
        q.append((1, 0))
        visited = set()
        while q:
            curr, moves = q.popleft()
            for i in range(1, 7):
                nxt = curr + i
                r, c = int_to_pos(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt == target:
                    return moves + 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, moves + 1))

        return -1
