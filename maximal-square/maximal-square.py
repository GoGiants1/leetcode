class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        
        # anti - diagonal
        mx = max(map(int,matrix[0]))
        for i in range(m):
            mx = max(int(matrix[i][0]), mx)
        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j] != 0:
                    if dp[i - 1][j] != 0 and dp[i][j - 1] != 0 and dp[i-1][j-1] != 0:
                        dp[i][j] = min(dp[i-1][j], dp[i][j -1], dp[i-1][j-1]) + 1
                    
                    mx = max(dp[i][j], mx)
        return mx ** 2