class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nr, nc = len(matrix), len(matrix[0])
        memo = [[None] * nc for i in range(nr)]
        
        def dp(i, j, memo):
            if i == nr or j == nc or j < 0:
                return math.inf
            if memo[i][j]:
                return memo[i][j]
            if i == nr - 1:
                memo[i][j] = matrix[i][j]
                return memo[i][j]
            
            memo[i][j] = matrix[i][j] + min(
                dp(i + 1, j - 1, memo), 
                dp(i + 1, j, memo),
                dp(i + 1, j + 1, memo)
                      
            )
            
            return memo[i][j]
        return min(dp(0, j, memo) for j in range(len(matrix[0])))
            