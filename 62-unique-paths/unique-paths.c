int uniquePaths(int m, int n) {
    int grid[m][n];

    // 중학교 수학 문제

    for(int i = 0; i < m; ++i){
        grid[i][0] = 1;    
    }
    for (int j = 0; j < n; ++j){
        grid[0][j] = 1;
    }

    // The test cases are generated so that the answer will be less than or equal to 2 * 10^9 = 2 * (2^10)^3 = 2^31. -> int32 보장

    for (int i = 1; i < m; ++i){
        for (int j = 1; j < n; ++j){
            grid[i][j] = grid[i-1][j] + grid[i][j-1];
        }
    }

    return grid[m-1][n-1];
}