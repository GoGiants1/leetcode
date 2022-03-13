class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        ans = 0

        for i in range(n):
            # Add elements from primary diagonal.
            ans += mat[i][i]
            # Add elements from secondary diagonal.
            ans += mat[n - 1 - i][i]
        # If n is odd, subtract the middle element as its added twice.
        if n % 2 != 0:
             ans -= mat[n // 2][n // 2]
        
        return ans
        # Two pass
        # # primary diag

        # x, y = 0, 0
        # s = 0
        # visit = set()
        # while x < r and y < c:
        #     s += mat[x][y]
        #     visit.add((x,y))
        #     x += 1
        #     y += 1
        
        # # secondary daig
        # x, y = 0, c - 1
        # while x < r and y >= 0:
        #     if (x,y) not in visit:
        #         s += mat[x][y]
        #     x += 1
        #     y -= 1
    
        # return s

        