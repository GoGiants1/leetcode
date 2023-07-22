class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),\
         (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        @cache
        def dp(r: int, c:int, remain: int):
            if remain == 0 and (0 <= r < n and 0 <= c < n):
                return 1
            if not (0 <= r < n and 0 <= c < n):
                return 0
            
            
            out = 0
            for move in moves:
                rr, cc = r + move[0], c + move[1]
                out += dp(rr, cc, remain - 1)
            return out

        return dp(row, column, k) / 8 ** k