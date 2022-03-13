class Solution:
    def totalNQueens(self, n: int) -> int:
        self.out = 0
        if n == 1:
            return 1

        def validate_pos(x, y):
            return 0 <= x < n and 0 <= y < n
        
        def placeQueen(prev_pos: int, cols: set, diag: set, anti_diag: set):
            def check(i, j):
                if j in cols or i + j in anti_diag or i - j in diag:
                    return False
                return True

            if len(cols) == n:
                print(prev_pos, cols, diag, anti_diag)
                self.out += 1
                return 

            start = 0 if prev_pos == -1 else prev_pos // n * n + n
            for curr in range(start, start + n):
                i, j = divmod(curr, n)
                if check(i,j):
                    cols.add(j)
                    diag.add(i-j)
                    anti_diag.add(i+j)
                    placeQueen(curr, cols, diag, anti_diag)
                    cols.remove(j)
                    diag.remove(i-j)
                    anti_diag.remove(i+j)
                curr += 1
            

            
        placeQueen(0, set(), set(), set())
        return self.out