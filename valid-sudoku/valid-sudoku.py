class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # r_check = [-1 for _ in range(9)]
        # c_check = [-1 for _ in range(9)]
        # blk_check = [-1 for _ in range(9)]

        
        # def row_check(r_idx):
        #     if r_check[r_idx] != -1:
        #         return r_check[r_idx]
        #     s = set()
        #     for v in board[r_idx]:
        #         if v == '.':
        #             continue
        #         if v in s:
        #             r_check[r_idx] = 0
        #             return 0
        #         s.add(v)
        #     r_check[r_idx] = 1
        #     return 1
        
        # def col_check(c_idx):
        #     if c_check[c_idx] != -1:
        #         return c_check[c_idx]
        #     s = set()
        #     for i in range(9):
        #         v = board[i][c_idx]
        #         if v == '.':
        #             continue
        #         if v in s:
        #             c_check[c_idx] = 0
        #             return 0
        #         s.add(v)
        #     c_check[c_idx] = 1
        #     return 1
        
        
        # def block_check(r, c):
        #     shr_r, _ = divmod(r, 3)
        #     shr_c, _ = divmod(c, 3)
        #     if blk_check[3 * shr_r + shr_c] != -1:
        #         return blk_check[3 * shr_r + shr_c]
            
        #     r = 3 * shr_r
        #     c = 3 * shr_c
        #     s = set()
        #     for dr in range(3):
        #         for dc in range(3):
        #             v = board[r+dr][c+dc]
        #             if v == '.':
        #                 continue
        #             if v in s:
        #                 blk_check[3 * shr_r + shr_c] = 0
        #                 return 0
        #             s.add(v)
        #     blk_check[3 * shr_r + shr_c] = 1
        #     return 1

        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == ".":
        #             continue
        #         else:
        #             r, c, b = row_check(i), col_check(j), block_check(i, j)
        #             for v in [r, c, b]:
        #                 print(r,c,b)
        #                 if v == 0:
        #                     return False
        # return True
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
                