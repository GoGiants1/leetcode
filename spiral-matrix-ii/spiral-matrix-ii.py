class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 완전 탐색
        mat = [[0 for _ in range(n)] for _ in range(n)]
        direction = [(0,1), (1,0), (-1, 0), (0,-1)]
        d_idx = 0
        r, c = 0, -1
        nn = n ** 2
        num = 1

        while num <= nn:
            d_idx %= 4
            dr, dc = direction[d_idx]
            if not (0 <= r + dr < n and 0 <= c + dc < n):
                d_idx += 1
            elif mat[r + dr][c + dc] != 0:
                d_idx += 1
            else:
                mat[r + dr][c + dc] = num
                r, c = r + dr, c + dc
                num += 1
        
        return mat
        
